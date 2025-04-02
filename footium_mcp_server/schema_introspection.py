import json
import asyncio
import os
from graphql import get_introspection_query, build_client_schema, print_schema
from footium_client import FootiumClient


async def fetch_schema(output_dir: str = "."):
    """Fetch and save the Footium GraphQL schema."""
    client = FootiumClient()
    introspection_query = get_introspection_query(descriptions=True)
    result = await client.execute(introspection_query)

    # Save raw schema data
    schema_json_path = os.path.join(output_dir, "schema.json")
    with open(schema_json_path, "w") as f:
        json.dump(result, f, indent=2)

    # Generate SDL file
    schema = build_client_schema(result["data"])
    schema_graphql_path = os.path.join(output_dir, "schema.graphql")
    with open(schema_graphql_path, "w") as f:
        f.write(print_schema(schema))

    print(f"Schema saved to {schema_json_path} and {schema_graphql_path}")

    return result["data"]["__schema"]


def analyze_schema(schema):
    """Analyze the schema to identify available queries and types."""
    query_type = schema["queryType"]
    query_type_name = query_type["name"]

    # Find the full query type definition
    query_type_def = next(
        (t for t in schema["types"] if t["name"] == query_type_name), None
    )

    if not query_type_def:
        print(f"Error: Could not find query type {query_type_name}")
        return []

    query_fields = query_type_def["fields"]

    print(f"\nAvailable queries ({len(query_fields)}):")
    for field in query_fields:
        args_str = ""
        if field.get("args"):
            args = []
            for arg in field["args"]:
                arg_type = get_type_name(arg["type"])
                args.append(f"{arg['name']}: {arg_type}")
            args_str = f"({', '.join(args)})"

        return_type = get_type_name(field["type"])
        print(f"  - {field['name']}{args_str}: {return_type}")
        if field.get("description"):
            print(f"    Description: {field['description']}")

    return query_fields


def get_type_name(type_obj):
    """Recursively build a type name from a GraphQL type object."""
    kind = type_obj["kind"]

    if kind == "NON_NULL":
        return f"{get_type_name(type_obj['ofType'])}!"
    elif kind == "LIST":
        return f"[{get_type_name(type_obj['ofType'])}]"
    else:
        return type_obj["name"]


def generate_resource_template(query):
    """Generate a template MCP resource for a GraphQL query."""
    name = query["name"]
    args = query.get("args", [])

    # Generate path parameters for the resource URI
    path_params = []
    args_dict = []

    for arg in args:
        arg_name = arg["name"]
        path_params.append(f"{{{arg_name}}}")
        args_dict.append(f'        "{arg_name}": {arg_name}')

    path_param_str = "/".join(path_params) if path_params else ""
    if path_param_str:
        resource_uri = f"footium://{name}/{path_param_str}"
    else:
        resource_uri = f"footium://{name}"

    # Generate function parameters
    fn_params = []
    for arg in args:
        arg_name = arg["name"]
        type_name = get_type_name(arg["type"])
        python_type = "str"  # Default

        if "Int" in type_name:
            python_type = "int"
        elif "Float" in type_name:
            python_type = "float"
        elif "Boolean" in type_name:
            python_type = "bool"

        fn_params.append(f"{arg_name}: {python_type}")

    fn_params_str = ", ".join(fn_params)

    # Build GraphQL query argument string for the query declaration
    query_args = ""
    if args:
        arg_declarations = []
        for arg in args:
            arg_declarations.append(f"${arg['name']}: {get_type_name(arg['type'])}")
        query_args = f"({', '.join(arg_declarations)})"

    # Build arguments for the actual field query
    field_args = ""
    if args:
        field_arg_list = []
        for arg in args:
            field_arg_list.append(f"{arg['name']}: ${arg['name']}")
        field_args = f"({', '.join(field_arg_list)})"

    # Generate docstring
    docstring = query.get("description", f"Get information about {name}")

    # Build the template
    template = f'@mcp.resource("{resource_uri}")\n'
    template += f"async def get_{name}({fn_params_str}) -> Dict[str, Any]:\n"
    template += f'    """{docstring}"""\n'
    template += f'    query = """\n'
    template += f"    query{query_args} {{\n"
    template += f"      {name}{field_args} {{\n"
    template += f"        # Add fields here based on the schema\n"
    template += f"        id\n"
    template += f"        name\n"
    template += f"      }}\n"
    template += f"    }}\n"
    template += f'    """\n'

    # Add variables if needed
    if args_dict:
        template += f"    variables = {{\n"
        for line in args_dict:
            template += f"{line},\n"
        template += f"    }}\n"
        template += f"    result = await client.execute(query, variables)\n"
    else:
        template += f"    result = await client.execute(query)\n"

    template += f'    return result.get("data", {{}}).get("{name}", {{}})\n'

    return template


def generate_mcp_resources(query_fields):
    """Generate MCP resource code for all query fields."""
    resources = []

    for query in sorted(query_fields, key=lambda q: q["name"]):
        resources.append(generate_resource_template(query))

    return "\n".join(resources)


async def run_introspection():
    """Run the introspection process and print results."""
    print("Fetching Footium GraphQL schema...")
    schema = await fetch_schema()

    print("\nAnalyzing schema...")
    query_fields = analyze_schema(schema)

    if query_fields:
        print("\nGenerating MCP resource templates...")
        resources_code = generate_mcp_resources(query_fields)

        with open("mcp_resources_template.py", "w") as f:
            f.write(resources_code)

        print(f"MCP resource templates saved to mcp_resources_template.py")

    return schema, query_fields


if __name__ == "__main__":
    asyncio.run(run_introspection())
