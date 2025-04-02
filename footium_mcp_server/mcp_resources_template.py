@mcp.resource("footium://academyMerkleRoot")
async def get_academyMerkleRoot() -> Dict[str, Any]:
    """None"""
    query = """
    query {
      academyMerkleRoot {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    result = await client.execute(query)
    return result.get("data", {}).get("academyMerkleRoot", {})

@mcp.resource("footium://academyMerkleRootToCommit")
async def get_academyMerkleRootToCommit() -> Dict[str, Any]:
    """None"""
    query = """
    query {
      academyMerkleRootToCommit {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    result = await client.execute(query)
    return result.get("data", {}).get("academyMerkleRootToCommit", {})

@mcp.resource("footium://academyPlayerMerkleProof/{playerId}")
async def get_academyPlayerMerkleProof(playerId: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($playerId: String!) {
      academyPlayerMerkleProof(playerId: $playerId) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "playerId": playerId,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("academyPlayerMerkleProof", {})

@mcp.resource("footium://actions/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_actions(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: ActionWhereInput, $orderBy: [ActionOrderByWithRelationInput!], $cursor: ActionWhereUniqueInput, $take: Int, $skip: Int, $distinct: [ActionScalarFieldEnum!]) {
      actions(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("actions", {})

@mcp.resource("footium://aggregateFixture/{where}/{orderBy}/{cursor}/{take}/{skip}")
async def get_aggregateFixture(where: str, orderBy: str, cursor: str, take: int, skip: int) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: FixtureWhereInput, $orderBy: [FixtureOrderByWithRelationInput!], $cursor: FixtureWhereUniqueInput, $take: Int, $skip: Int) {
      aggregateFixture(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("aggregateFixture", {})

@mcp.resource("footium://allClubsBasicInfo/{ownerAddress}")
async def get_allClubsBasicInfo(ownerAddress: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($ownerAddress: String!) {
      allClubsBasicInfo(ownerAddress: $ownerAddress) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "ownerAddress": ownerAddress,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("allClubsBasicInfo", {})

@mcp.resource("footium://amateurClubs")
async def get_amateurClubs() -> Dict[str, Any]:
    """None"""
    query = """
    query {
      amateurClubs {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    result = await client.execute(query)
    return result.get("data", {}).get("amateurClubs", {})

@mcp.resource("footium://availableHomeGameTime/{where}")
async def get_availableHomeGameTime(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: AvailableHomeGameTimeWhereUniqueInput!) {
      availableHomeGameTime(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("availableHomeGameTime", {})

@mcp.resource("footium://availableHomeGameTimes/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_availableHomeGameTimes(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: AvailableHomeGameTimeWhereInput, $orderBy: [AvailableHomeGameTimeOrderByWithRelationInput!], $cursor: AvailableHomeGameTimeWhereUniqueInput, $take: Int, $skip: Int, $distinct: [AvailableHomeGameTimeScalarFieldEnum!]) {
      availableHomeGameTimes(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("availableHomeGameTimes", {})

@mcp.resource("footium://club/{where}")
async def get_club(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: ClubWhereUniqueInput!) {
      club(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("club", {})

@mcp.resource("footium://clubBadge/{where}")
async def get_clubBadge(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: ClubBadgeWhereUniqueInput!) {
      clubBadge(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("clubBadge", {})

@mcp.resource("footium://clubBadges/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_clubBadges(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: ClubBadgeWhereInput, $orderBy: [ClubBadgeOrderByWithRelationInput!], $cursor: ClubBadgeWhereUniqueInput, $take: Int, $skip: Int, $distinct: [ClubBadgeScalarFieldEnum!]) {
      clubBadges(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("clubBadges", {})

@mcp.resource("footium://clubFixture/{where}")
async def get_clubFixture(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: ClubFixtureWhereUniqueInput!) {
      clubFixture(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("clubFixture", {})

@mcp.resource("footium://clubFixtures/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_clubFixtures(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: ClubFixtureWhereInput, $orderBy: [ClubFixtureOrderByWithRelationInput!], $cursor: ClubFixtureWhereUniqueInput, $take: Int, $skip: Int, $distinct: [ClubFixtureScalarFieldEnum!]) {
      clubFixtures(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("clubFixtures", {})

@mcp.resource("footium://clubTournament/{where}")
async def get_clubTournament(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: ClubTournamentWhereUniqueInput!) {
      clubTournament(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("clubTournament", {})

@mcp.resource("footium://clubs/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_clubs(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: ClubWhereInput, $orderBy: [ClubOrderByWithRelationInput!], $cursor: ClubWhereUniqueInput, $take: Int, $skip: Int, $distinct: [ClubScalarFieldEnum!]) {
      clubs(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("clubs", {})

@mcp.resource("footium://clubsFlaggedForRemoval")
async def get_clubsFlaggedForRemoval() -> Dict[str, Any]:
    """None"""
    query = """
    query {
      clubsFlaggedForRemoval {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    result = await client.execute(query)
    return result.get("data", {}).get("clubsFlaggedForRemoval", {})

@mcp.resource("footium://competition/{where}")
async def get_competition(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: CompetitionWhereUniqueInput!) {
      competition(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("competition", {})

@mcp.resource("footium://competitions/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_competitions(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: CompetitionWhereInput, $orderBy: [CompetitionOrderByWithRelationInput!], $cursor: CompetitionWhereUniqueInput, $take: Int, $skip: Int, $distinct: [CompetitionScalarFieldEnum!]) {
      competitions(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("competitions", {})

@mcp.resource("footium://division/{where}")
async def get_division(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: DivisionWhereUniqueInput!) {
      division(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("division", {})

@mcp.resource("footium://divisions/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_divisions(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: DivisionWhereInput, $orderBy: [DivisionOrderByWithRelationInput!], $cursor: DivisionWhereUniqueInput, $take: Int, $skip: Int, $distinct: [DivisionScalarFieldEnum!]) {
      divisions(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("divisions", {})

@mcp.resource("footium://ethereumEvents/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_ethereumEvents(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: EthereumEventWhereInput, $orderBy: [EthereumEventOrderByWithRelationInput!], $cursor: EthereumEventWhereUniqueInput, $take: Int, $skip: Int, $distinct: [EthereumEventScalarFieldEnum!]) {
      ethereumEvents(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("ethereumEvents", {})

@mcp.resource("footium://findFirstAvailableHomeGameTime/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstAvailableHomeGameTime(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: AvailableHomeGameTimeWhereInput, $orderBy: [AvailableHomeGameTimeOrderByWithRelationInput!], $cursor: AvailableHomeGameTimeWhereUniqueInput, $take: Int, $skip: Int, $distinct: [AvailableHomeGameTimeScalarFieldEnum!]) {
      findFirstAvailableHomeGameTime(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstAvailableHomeGameTime", {})

@mcp.resource("footium://findFirstAvailableHomeGameTimeOrThrow/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstAvailableHomeGameTimeOrThrow(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: AvailableHomeGameTimeWhereInput, $orderBy: [AvailableHomeGameTimeOrderByWithRelationInput!], $cursor: AvailableHomeGameTimeWhereUniqueInput, $take: Int, $skip: Int, $distinct: [AvailableHomeGameTimeScalarFieldEnum!]) {
      findFirstAvailableHomeGameTimeOrThrow(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstAvailableHomeGameTimeOrThrow", {})

@mcp.resource("footium://findFirstClub/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstClub(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: ClubWhereInput, $orderBy: [ClubOrderByWithRelationInput!], $cursor: ClubWhereUniqueInput, $take: Int, $skip: Int, $distinct: [ClubScalarFieldEnum!]) {
      findFirstClub(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstClub", {})

@mcp.resource("footium://findFirstClubBadge/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstClubBadge(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: ClubBadgeWhereInput, $orderBy: [ClubBadgeOrderByWithRelationInput!], $cursor: ClubBadgeWhereUniqueInput, $take: Int, $skip: Int, $distinct: [ClubBadgeScalarFieldEnum!]) {
      findFirstClubBadge(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstClubBadge", {})

@mcp.resource("footium://findFirstClubBadgeOrThrow/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstClubBadgeOrThrow(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: ClubBadgeWhereInput, $orderBy: [ClubBadgeOrderByWithRelationInput!], $cursor: ClubBadgeWhereUniqueInput, $take: Int, $skip: Int, $distinct: [ClubBadgeScalarFieldEnum!]) {
      findFirstClubBadgeOrThrow(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstClubBadgeOrThrow", {})

@mcp.resource("footium://findFirstClubFixture/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstClubFixture(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: ClubFixtureWhereInput, $orderBy: [ClubFixtureOrderByWithRelationInput!], $cursor: ClubFixtureWhereUniqueInput, $take: Int, $skip: Int, $distinct: [ClubFixtureScalarFieldEnum!]) {
      findFirstClubFixture(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstClubFixture", {})

@mcp.resource("footium://findFirstClubFixtureOrThrow/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstClubFixtureOrThrow(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: ClubFixtureWhereInput, $orderBy: [ClubFixtureOrderByWithRelationInput!], $cursor: ClubFixtureWhereUniqueInput, $take: Int, $skip: Int, $distinct: [ClubFixtureScalarFieldEnum!]) {
      findFirstClubFixtureOrThrow(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstClubFixtureOrThrow", {})

@mcp.resource("footium://findFirstClubOrThrow/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstClubOrThrow(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: ClubWhereInput, $orderBy: [ClubOrderByWithRelationInput!], $cursor: ClubWhereUniqueInput, $take: Int, $skip: Int, $distinct: [ClubScalarFieldEnum!]) {
      findFirstClubOrThrow(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstClubOrThrow", {})

@mcp.resource("footium://findFirstClubStats/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstClubStats(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: ClubStatsWhereInput, $orderBy: [ClubStatsOrderByWithRelationInput!], $cursor: ClubStatsWhereUniqueInput, $take: Int, $skip: Int, $distinct: [ClubStatsScalarFieldEnum!]) {
      findFirstClubStats(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstClubStats", {})

@mcp.resource("footium://findFirstClubStatsOrThrow/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstClubStatsOrThrow(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: ClubStatsWhereInput, $orderBy: [ClubStatsOrderByWithRelationInput!], $cursor: ClubStatsWhereUniqueInput, $take: Int, $skip: Int, $distinct: [ClubStatsScalarFieldEnum!]) {
      findFirstClubStatsOrThrow(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstClubStatsOrThrow", {})

@mcp.resource("footium://findFirstClubTournament/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstClubTournament(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: ClubTournamentWhereInput, $orderBy: [ClubTournamentOrderByWithRelationInput!], $cursor: ClubTournamentWhereUniqueInput, $take: Int, $skip: Int, $distinct: [ClubTournamentScalarFieldEnum!]) {
      findFirstClubTournament(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstClubTournament", {})

@mcp.resource("footium://findFirstClubTournamentOrThrow/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstClubTournamentOrThrow(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: ClubTournamentWhereInput, $orderBy: [ClubTournamentOrderByWithRelationInput!], $cursor: ClubTournamentWhereUniqueInput, $take: Int, $skip: Int, $distinct: [ClubTournamentScalarFieldEnum!]) {
      findFirstClubTournamentOrThrow(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstClubTournamentOrThrow", {})

@mcp.resource("footium://findFirstCompetition/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstCompetition(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: CompetitionWhereInput, $orderBy: [CompetitionOrderByWithRelationInput!], $cursor: CompetitionWhereUniqueInput, $take: Int, $skip: Int, $distinct: [CompetitionScalarFieldEnum!]) {
      findFirstCompetition(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstCompetition", {})

@mcp.resource("footium://findFirstCompetitionOrThrow/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstCompetitionOrThrow(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: CompetitionWhereInput, $orderBy: [CompetitionOrderByWithRelationInput!], $cursor: CompetitionWhereUniqueInput, $take: Int, $skip: Int, $distinct: [CompetitionScalarFieldEnum!]) {
      findFirstCompetitionOrThrow(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstCompetitionOrThrow", {})

@mcp.resource("footium://findFirstDivision/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstDivision(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: DivisionWhereInput, $orderBy: [DivisionOrderByWithRelationInput!], $cursor: DivisionWhereUniqueInput, $take: Int, $skip: Int, $distinct: [DivisionScalarFieldEnum!]) {
      findFirstDivision(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstDivision", {})

@mcp.resource("footium://findFirstDivisionOrThrow/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstDivisionOrThrow(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: DivisionWhereInput, $orderBy: [DivisionOrderByWithRelationInput!], $cursor: DivisionWhereUniqueInput, $take: Int, $skip: Int, $distinct: [DivisionScalarFieldEnum!]) {
      findFirstDivisionOrThrow(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstDivisionOrThrow", {})

@mcp.resource("footium://findFirstFixture/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstFixture(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: FixtureWhereInput, $orderBy: [FixtureOrderByWithRelationInput!], $cursor: FixtureWhereUniqueInput, $take: Int, $skip: Int, $distinct: [FixtureScalarFieldEnum!]) {
      findFirstFixture(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstFixture", {})

@mcp.resource("footium://findFirstFixtureOrThrow/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstFixtureOrThrow(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: FixtureWhereInput, $orderBy: [FixtureOrderByWithRelationInput!], $cursor: FixtureWhereUniqueInput, $take: Int, $skip: Int, $distinct: [FixtureScalarFieldEnum!]) {
      findFirstFixtureOrThrow(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstFixtureOrThrow", {})

@mcp.resource("footium://findFirstFormation/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstFormation(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: FormationWhereInput, $orderBy: [FormationOrderByWithRelationInput!], $cursor: FormationWhereUniqueInput, $take: Int, $skip: Int, $distinct: [FormationScalarFieldEnum!]) {
      findFirstFormation(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstFormation", {})

@mcp.resource("footium://findFirstFormationOrThrow/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstFormationOrThrow(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: FormationWhereInput, $orderBy: [FormationOrderByWithRelationInput!], $cursor: FormationWhereUniqueInput, $take: Int, $skip: Int, $distinct: [FormationScalarFieldEnum!]) {
      findFirstFormationOrThrow(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstFormationOrThrow", {})

@mcp.resource("footium://findFirstFormationSlot/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstFormationSlot(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: FormationSlotWhereInput, $orderBy: [FormationSlotOrderByWithRelationInput!], $cursor: FormationSlotWhereUniqueInput, $take: Int, $skip: Int, $distinct: [FormationSlotScalarFieldEnum!]) {
      findFirstFormationSlot(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstFormationSlot", {})

@mcp.resource("footium://findFirstFormationSlotOrThrow/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstFormationSlotOrThrow(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: FormationSlotWhereInput, $orderBy: [FormationSlotOrderByWithRelationInput!], $cursor: FormationSlotWhereUniqueInput, $take: Int, $skip: Int, $distinct: [FormationSlotScalarFieldEnum!]) {
      findFirstFormationSlotOrThrow(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstFormationSlotOrThrow", {})

@mcp.resource("footium://findFirstKit/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstKit(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: KitWhereInput, $orderBy: [KitOrderByWithRelationInput!], $cursor: KitWhereUniqueInput, $take: Int, $skip: Int, $distinct: [KitScalarFieldEnum!]) {
      findFirstKit(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstKit", {})

@mcp.resource("footium://findFirstKitOrThrow/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstKitOrThrow(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: KitWhereInput, $orderBy: [KitOrderByWithRelationInput!], $cursor: KitWhereUniqueInput, $take: Int, $skip: Int, $distinct: [KitScalarFieldEnum!]) {
      findFirstKitOrThrow(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstKitOrThrow", {})

@mcp.resource("footium://findFirstLineup/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstLineup(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: LineupWhereInput, $orderBy: [LineupOrderByWithRelationInput!], $cursor: LineupWhereUniqueInput, $take: Int, $skip: Int, $distinct: [LineupScalarFieldEnum!]) {
      findFirstLineup(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstLineup", {})

@mcp.resource("footium://findFirstLineupOrThrow/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstLineupOrThrow(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: LineupWhereInput, $orderBy: [LineupOrderByWithRelationInput!], $cursor: LineupWhereUniqueInput, $take: Int, $skip: Int, $distinct: [LineupScalarFieldEnum!]) {
      findFirstLineupOrThrow(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstLineupOrThrow", {})

@mcp.resource("footium://findFirstMatch/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstMatch(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: MatchWhereInput, $orderBy: [MatchOrderByWithRelationInput!], $cursor: MatchWhereUniqueInput, $take: Int, $skip: Int, $distinct: [MatchScalarFieldEnum!]) {
      findFirstMatch(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstMatch", {})

@mcp.resource("footium://findFirstMatchChange/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstMatchChange(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: MatchChangeWhereInput, $orderBy: [MatchChangeOrderByWithRelationInput!], $cursor: MatchChangeWhereUniqueInput, $take: Int, $skip: Int, $distinct: [MatchChangeScalarFieldEnum!]) {
      findFirstMatchChange(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstMatchChange", {})

@mcp.resource("footium://findFirstMatchChangeOrThrow/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstMatchChangeOrThrow(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: MatchChangeWhereInput, $orderBy: [MatchChangeOrderByWithRelationInput!], $cursor: MatchChangeWhereUniqueInput, $take: Int, $skip: Int, $distinct: [MatchChangeScalarFieldEnum!]) {
      findFirstMatchChangeOrThrow(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstMatchChangeOrThrow", {})

@mcp.resource("footium://findFirstMatchConfiguration/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstMatchConfiguration(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: MatchConfigurationWhereInput, $orderBy: [MatchConfigurationOrderByWithRelationInput!], $cursor: MatchConfigurationWhereUniqueInput, $take: Int, $skip: Int, $distinct: [MatchConfigurationScalarFieldEnum!]) {
      findFirstMatchConfiguration(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstMatchConfiguration", {})

@mcp.resource("footium://findFirstMatchConfigurationOrThrow/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstMatchConfigurationOrThrow(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: MatchConfigurationWhereInput, $orderBy: [MatchConfigurationOrderByWithRelationInput!], $cursor: MatchConfigurationWhereUniqueInput, $take: Int, $skip: Int, $distinct: [MatchConfigurationScalarFieldEnum!]) {
      findFirstMatchConfigurationOrThrow(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstMatchConfigurationOrThrow", {})

@mcp.resource("footium://findFirstMatchOrThrow/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstMatchOrThrow(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: MatchWhereInput, $orderBy: [MatchOrderByWithRelationInput!], $cursor: MatchWhereUniqueInput, $take: Int, $skip: Int, $distinct: [MatchScalarFieldEnum!]) {
      findFirstMatchOrThrow(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstMatchOrThrow", {})

@mcp.resource("footium://findFirstMerkleRoot/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstMerkleRoot(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: MerkleRootWhereInput, $orderBy: [MerkleRootOrderByWithRelationInput!], $cursor: MerkleRootWhereUniqueInput, $take: Int, $skip: Int, $distinct: [MerkleRootScalarFieldEnum!]) {
      findFirstMerkleRoot(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstMerkleRoot", {})

@mcp.resource("footium://findFirstMerkleRootOrThrow/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstMerkleRootOrThrow(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: MerkleRootWhereInput, $orderBy: [MerkleRootOrderByWithRelationInput!], $cursor: MerkleRootWhereUniqueInput, $take: Int, $skip: Int, $distinct: [MerkleRootScalarFieldEnum!]) {
      findFirstMerkleRootOrThrow(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstMerkleRootOrThrow", {})

@mcp.resource("footium://findFirstMetadata/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstMetadata(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: MetadataWhereInput, $orderBy: [MetadataOrderByWithRelationInput!], $cursor: MetadataWhereUniqueInput, $take: Int, $skip: Int, $distinct: [MetadataScalarFieldEnum!]) {
      findFirstMetadata(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstMetadata", {})

@mcp.resource("footium://findFirstMetadataOrThrow/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstMetadataOrThrow(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: MetadataWhereInput, $orderBy: [MetadataOrderByWithRelationInput!], $cursor: MetadataWhereUniqueInput, $take: Int, $skip: Int, $distinct: [MetadataScalarFieldEnum!]) {
      findFirstMetadataOrThrow(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstMetadataOrThrow", {})

@mcp.resource("footium://findFirstOwner/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstOwner(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: OwnerWhereInput, $orderBy: [OwnerOrderByWithRelationInput!], $cursor: OwnerWhereUniqueInput, $take: Int, $skip: Int, $distinct: [OwnerScalarFieldEnum!]) {
      findFirstOwner(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstOwner", {})

@mcp.resource("footium://findFirstOwnerOrThrow/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstOwnerOrThrow(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: OwnerWhereInput, $orderBy: [OwnerOrderByWithRelationInput!], $cursor: OwnerWhereUniqueInput, $take: Int, $skip: Int, $distinct: [OwnerScalarFieldEnum!]) {
      findFirstOwnerOrThrow(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstOwnerOrThrow", {})

@mcp.resource("footium://findFirstPlayer/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstPlayer(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PlayerWhereInput, $orderBy: [PlayerOrderByWithRelationInput!], $cursor: PlayerWhereUniqueInput, $take: Int, $skip: Int, $distinct: [PlayerScalarFieldEnum!]) {
      findFirstPlayer(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstPlayer", {})

@mcp.resource("footium://findFirstPlayerAttributes/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstPlayerAttributes(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PlayerAttributesWhereInput, $orderBy: [PlayerAttributesOrderByWithRelationInput!], $cursor: PlayerAttributesWhereUniqueInput, $take: Int, $skip: Int, $distinct: [PlayerAttributesScalarFieldEnum!]) {
      findFirstPlayerAttributes(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstPlayerAttributes", {})

@mcp.resource("footium://findFirstPlayerAttributesOrThrow/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstPlayerAttributesOrThrow(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PlayerAttributesWhereInput, $orderBy: [PlayerAttributesOrderByWithRelationInput!], $cursor: PlayerAttributesWhereUniqueInput, $take: Int, $skip: Int, $distinct: [PlayerAttributesScalarFieldEnum!]) {
      findFirstPlayerAttributesOrThrow(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstPlayerAttributesOrThrow", {})

@mcp.resource("footium://findFirstPlayerLineup/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstPlayerLineup(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PlayerLineupWhereInput, $orderBy: [PlayerLineupOrderByWithRelationInput!], $cursor: PlayerLineupWhereUniqueInput, $take: Int, $skip: Int, $distinct: [PlayerLineupScalarFieldEnum!]) {
      findFirstPlayerLineup(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstPlayerLineup", {})

@mcp.resource("footium://findFirstPlayerLineupOrThrow/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstPlayerLineupOrThrow(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PlayerLineupWhereInput, $orderBy: [PlayerLineupOrderByWithRelationInput!], $cursor: PlayerLineupWhereUniqueInput, $take: Int, $skip: Int, $distinct: [PlayerLineupScalarFieldEnum!]) {
      findFirstPlayerLineupOrThrow(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstPlayerLineupOrThrow", {})

@mcp.resource("footium://findFirstPlayerOrThrow/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstPlayerOrThrow(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PlayerWhereInput, $orderBy: [PlayerOrderByWithRelationInput!], $cursor: PlayerWhereUniqueInput, $take: Int, $skip: Int, $distinct: [PlayerScalarFieldEnum!]) {
      findFirstPlayerOrThrow(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstPlayerOrThrow", {})

@mcp.resource("footium://findFirstPlayerRegistration/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstPlayerRegistration(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PlayerRegistrationWhereInput, $orderBy: [PlayerRegistrationOrderByWithRelationInput!], $cursor: PlayerRegistrationWhereUniqueInput, $take: Int, $skip: Int, $distinct: [PlayerRegistrationScalarFieldEnum!]) {
      findFirstPlayerRegistration(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstPlayerRegistration", {})

@mcp.resource("footium://findFirstPlayerRegistrationOrThrow/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstPlayerRegistrationOrThrow(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PlayerRegistrationWhereInput, $orderBy: [PlayerRegistrationOrderByWithRelationInput!], $cursor: PlayerRegistrationWhereUniqueInput, $take: Int, $skip: Int, $distinct: [PlayerRegistrationScalarFieldEnum!]) {
      findFirstPlayerRegistrationOrThrow(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstPlayerRegistrationOrThrow", {})

@mcp.resource("footium://findFirstPositionalRating/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstPositionalRating(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PositionalRatingWhereInput, $orderBy: [PositionalRatingOrderByWithRelationInput!], $cursor: PositionalRatingWhereUniqueInput, $take: Int, $skip: Int, $distinct: [PositionalRatingScalarFieldEnum!]) {
      findFirstPositionalRating(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstPositionalRating", {})

@mcp.resource("footium://findFirstPositionalRatingOrThrow/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstPositionalRatingOrThrow(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PositionalRatingWhereInput, $orderBy: [PositionalRatingOrderByWithRelationInput!], $cursor: PositionalRatingWhereUniqueInput, $take: Int, $skip: Int, $distinct: [PositionalRatingScalarFieldEnum!]) {
      findFirstPositionalRatingOrThrow(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstPositionalRatingOrThrow", {})

@mcp.resource("footium://findFirstPrize/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstPrize(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PrizeWhereInput, $orderBy: [PrizeOrderByWithRelationInput!], $cursor: PrizeWhereUniqueInput, $take: Int, $skip: Int, $distinct: [PrizeScalarFieldEnum!]) {
      findFirstPrize(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstPrize", {})

@mcp.resource("footium://findFirstPrizeAssignment/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstPrizeAssignment(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PrizeAssignmentWhereInput, $orderBy: [PrizeAssignmentOrderByWithRelationInput!], $cursor: PrizeAssignmentWhereUniqueInput, $take: Int, $skip: Int, $distinct: [PrizeAssignmentScalarFieldEnum!]) {
      findFirstPrizeAssignment(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstPrizeAssignment", {})

@mcp.resource("footium://findFirstPrizeAssignmentOrThrow/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstPrizeAssignmentOrThrow(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PrizeAssignmentWhereInput, $orderBy: [PrizeAssignmentOrderByWithRelationInput!], $cursor: PrizeAssignmentWhereUniqueInput, $take: Int, $skip: Int, $distinct: [PrizeAssignmentScalarFieldEnum!]) {
      findFirstPrizeAssignmentOrThrow(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstPrizeAssignmentOrThrow", {})

@mcp.resource("footium://findFirstPrizeClaim/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstPrizeClaim(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PrizeClaimWhereInput, $orderBy: [PrizeClaimOrderByWithRelationInput!], $cursor: PrizeClaimWhereUniqueInput, $take: Int, $skip: Int, $distinct: [PrizeClaimScalarFieldEnum!]) {
      findFirstPrizeClaim(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstPrizeClaim", {})

@mcp.resource("footium://findFirstPromotionSelector/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstPromotionSelector(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PromotionSelectorWhereInput, $orderBy: [PromotionSelectorOrderByWithRelationInput!], $cursor: PromotionSelectorWhereUniqueInput, $take: Int, $skip: Int, $distinct: [PromotionSelectorScalarFieldEnum!]) {
      findFirstPromotionSelector(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstPromotionSelector", {})

@mcp.resource("footium://findFirstPromotionSelectorOrThrow/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstPromotionSelectorOrThrow(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PromotionSelectorWhereInput, $orderBy: [PromotionSelectorOrderByWithRelationInput!], $cursor: PromotionSelectorWhereUniqueInput, $take: Int, $skip: Int, $distinct: [PromotionSelectorScalarFieldEnum!]) {
      findFirstPromotionSelectorOrThrow(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstPromotionSelectorOrThrow", {})

@mcp.resource("footium://findFirstRegistrationWindow/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstRegistrationWindow(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: RegistrationWindowWhereInput, $orderBy: [RegistrationWindowOrderByWithRelationInput!], $cursor: RegistrationWindowWhereUniqueInput, $take: Int, $skip: Int, $distinct: [RegistrationWindowScalarFieldEnum!]) {
      findFirstRegistrationWindow(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstRegistrationWindow", {})

@mcp.resource("footium://findFirstRegistrationWindowOrThrow/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstRegistrationWindowOrThrow(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: RegistrationWindowWhereInput, $orderBy: [RegistrationWindowOrderByWithRelationInput!], $cursor: RegistrationWindowWhereUniqueInput, $take: Int, $skip: Int, $distinct: [RegistrationWindowScalarFieldEnum!]) {
      findFirstRegistrationWindowOrThrow(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstRegistrationWindowOrThrow", {})

@mcp.resource("footium://findFirstSeason/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstSeason(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: SeasonWhereInput, $orderBy: [SeasonOrderByWithRelationInput!], $cursor: SeasonWhereUniqueInput, $take: Int, $skip: Int, $distinct: [SeasonScalarFieldEnum!]) {
      findFirstSeason(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstSeason", {})

@mcp.resource("footium://findFirstSeasonOrThrow/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstSeasonOrThrow(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: SeasonWhereInput, $orderBy: [SeasonOrderByWithRelationInput!], $cursor: SeasonWhereUniqueInput, $take: Int, $skip: Int, $distinct: [SeasonScalarFieldEnum!]) {
      findFirstSeasonOrThrow(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstSeasonOrThrow", {})

@mcp.resource("footium://findFirstStadium/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstStadium(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: StadiumWhereInput, $orderBy: [StadiumOrderByWithRelationInput!], $cursor: StadiumWhereUniqueInput, $take: Int, $skip: Int, $distinct: [StadiumScalarFieldEnum!]) {
      findFirstStadium(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstStadium", {})

@mcp.resource("footium://findFirstStadiumOrThrow/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstStadiumOrThrow(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: StadiumWhereInput, $orderBy: [StadiumOrderByWithRelationInput!], $cursor: StadiumWhereUniqueInput, $take: Int, $skip: Int, $distinct: [StadiumScalarFieldEnum!]) {
      findFirstStadiumOrThrow(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstStadiumOrThrow", {})

@mcp.resource("footium://findFirstStadiumStand/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstStadiumStand(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: StadiumStandWhereInput, $orderBy: [StadiumStandOrderByWithRelationInput!], $cursor: StadiumStandWhereUniqueInput, $take: Int, $skip: Int, $distinct: [StadiumStandScalarFieldEnum!]) {
      findFirstStadiumStand(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstStadiumStand", {})

@mcp.resource("footium://findFirstStadiumStandOrThrow/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstStadiumStandOrThrow(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: StadiumStandWhereInput, $orderBy: [StadiumStandOrderByWithRelationInput!], $cursor: StadiumStandWhereUniqueInput, $take: Int, $skip: Int, $distinct: [StadiumStandScalarFieldEnum!]) {
      findFirstStadiumStandOrThrow(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstStadiumStandOrThrow", {})

@mcp.resource("footium://findFirstTactics/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstTactics(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: TacticsWhereInput, $orderBy: [TacticsOrderByWithRelationInput!], $cursor: TacticsWhereUniqueInput, $take: Int, $skip: Int, $distinct: [TacticsScalarFieldEnum!]) {
      findFirstTactics(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstTactics", {})

@mcp.resource("footium://findFirstTacticsOrThrow/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstTacticsOrThrow(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: TacticsWhereInput, $orderBy: [TacticsOrderByWithRelationInput!], $cursor: TacticsWhereUniqueInput, $take: Int, $skip: Int, $distinct: [TacticsScalarFieldEnum!]) {
      findFirstTacticsOrThrow(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstTacticsOrThrow", {})

@mcp.resource("footium://findFirstTournament/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstTournament(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: TournamentWhereInput, $orderBy: [TournamentOrderByWithRelationInput!], $cursor: TournamentWhereUniqueInput, $take: Int, $skip: Int, $distinct: [TournamentScalarFieldEnum!]) {
      findFirstTournament(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstTournament", {})

@mcp.resource("footium://findFirstTournamentOrThrow/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstTournamentOrThrow(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: TournamentWhereInput, $orderBy: [TournamentOrderByWithRelationInput!], $cursor: TournamentWhereUniqueInput, $take: Int, $skip: Int, $distinct: [TournamentScalarFieldEnum!]) {
      findFirstTournamentOrThrow(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstTournamentOrThrow", {})

@mcp.resource("footium://findFirstTournamentResult/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstTournamentResult(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: TournamentResultWhereInput, $orderBy: [TournamentResultOrderByWithRelationInput!], $cursor: TournamentResultWhereUniqueInput, $take: Int, $skip: Int, $distinct: [TournamentResultScalarFieldEnum!]) {
      findFirstTournamentResult(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstTournamentResult", {})

@mcp.resource("footium://findFirstTournamentResultOrThrow/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstTournamentResultOrThrow(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: TournamentResultWhereInput, $orderBy: [TournamentResultOrderByWithRelationInput!], $cursor: TournamentResultWhereUniqueInput, $take: Int, $skip: Int, $distinct: [TournamentResultScalarFieldEnum!]) {
      findFirstTournamentResultOrThrow(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstTournamentResultOrThrow", {})

@mcp.resource("footium://findFirstTrainingSlot/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstTrainingSlot(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: TrainingSlotWhereInput, $orderBy: [TrainingSlotOrderByWithRelationInput!], $cursor: TrainingSlotWhereUniqueInput, $take: Int, $skip: Int, $distinct: [TrainingSlotScalarFieldEnum!]) {
      findFirstTrainingSlot(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstTrainingSlot", {})

@mcp.resource("footium://findFirstTrainingSlotOrThrow/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_findFirstTrainingSlotOrThrow(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: TrainingSlotWhereInput, $orderBy: [TrainingSlotOrderByWithRelationInput!], $cursor: TrainingSlotWhereUniqueInput, $take: Int, $skip: Int, $distinct: [TrainingSlotScalarFieldEnum!]) {
      findFirstTrainingSlotOrThrow(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findFirstTrainingSlotOrThrow", {})

@mcp.resource("footium://findUniqueClubStats/{where}")
async def get_findUniqueClubStats(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: ClubStatsWhereUniqueInput!) {
      findUniqueClubStats(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findUniqueClubStats", {})

@mcp.resource("footium://findUniqueClubStatsOrThrow/{where}")
async def get_findUniqueClubStatsOrThrow(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: ClubStatsWhereUniqueInput!) {
      findUniqueClubStatsOrThrow(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findUniqueClubStatsOrThrow", {})

@mcp.resource("footium://findUniqueMetadata/{where}")
async def get_findUniqueMetadata(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: MetadataWhereUniqueInput!) {
      findUniqueMetadata(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findUniqueMetadata", {})

@mcp.resource("footium://findUniqueMetadataOrThrow/{where}")
async def get_findUniqueMetadataOrThrow(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: MetadataWhereUniqueInput!) {
      findUniqueMetadataOrThrow(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findUniqueMetadataOrThrow", {})

@mcp.resource("footium://findUniquePlayerAttributes/{where}")
async def get_findUniquePlayerAttributes(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PlayerAttributesWhereUniqueInput!) {
      findUniquePlayerAttributes(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findUniquePlayerAttributes", {})

@mcp.resource("footium://findUniquePlayerAttributesOrThrow/{where}")
async def get_findUniquePlayerAttributesOrThrow(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PlayerAttributesWhereUniqueInput!) {
      findUniquePlayerAttributesOrThrow(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findUniquePlayerAttributesOrThrow", {})

@mcp.resource("footium://findUniqueTactics/{where}")
async def get_findUniqueTactics(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: TacticsWhereUniqueInput!) {
      findUniqueTactics(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findUniqueTactics", {})

@mcp.resource("footium://findUniqueTacticsOrThrow/{where}")
async def get_findUniqueTacticsOrThrow(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: TacticsWhereUniqueInput!) {
      findUniqueTacticsOrThrow(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("findUniqueTacticsOrThrow", {})

@mcp.resource("footium://fixture/{where}")
async def get_fixture(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: FixtureWhereUniqueInput!) {
      fixture(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("fixture", {})

@mcp.resource("footium://fixtures/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_fixtures(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: FixtureWhereInput, $orderBy: [FixtureOrderByWithRelationInput!], $cursor: FixtureWhereUniqueInput, $take: Int, $skip: Int, $distinct: [FixtureScalarFieldEnum!]) {
      fixtures(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("fixtures", {})

@mcp.resource("footium://formation/{where}")
async def get_formation(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: FormationWhereUniqueInput!) {
      formation(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("formation", {})

@mcp.resource("footium://formationSlot/{where}")
async def get_formationSlot(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: FormationSlotWhereUniqueInput!) {
      formationSlot(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("formationSlot", {})

@mcp.resource("footium://formationSlots/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_formationSlots(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: FormationSlotWhereInput, $orderBy: [FormationSlotOrderByWithRelationInput!], $cursor: FormationSlotWhereUniqueInput, $take: Int, $skip: Int, $distinct: [FormationSlotScalarFieldEnum!]) {
      formationSlots(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("formationSlots", {})

@mcp.resource("footium://formations/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_formations(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: FormationWhereInput, $orderBy: [FormationOrderByWithRelationInput!], $cursor: FormationWhereUniqueInput, $take: Int, $skip: Int, $distinct: [FormationScalarFieldEnum!]) {
      formations(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("formations", {})

@mcp.resource("footium://gameState")
async def get_gameState() -> Dict[str, Any]:
    """None"""
    query = """
    query {
      gameState {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    result = await client.execute(query)
    return result.get("data", {}).get("gameState", {})

@mcp.resource("footium://getAvailableHomeGameTime/{where}")
async def get_getAvailableHomeGameTime(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: AvailableHomeGameTimeWhereUniqueInput!) {
      getAvailableHomeGameTime(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("getAvailableHomeGameTime", {})

@mcp.resource("footium://getClub/{where}")
async def get_getClub(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: ClubWhereUniqueInput!) {
      getClub(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("getClub", {})

@mcp.resource("footium://getClubBadge/{where}")
async def get_getClubBadge(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: ClubBadgeWhereUniqueInput!) {
      getClubBadge(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("getClubBadge", {})

@mcp.resource("footium://getClubFixture/{where}")
async def get_getClubFixture(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: ClubFixtureWhereUniqueInput!) {
      getClubFixture(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("getClubFixture", {})

@mcp.resource("footium://getClubTournament/{where}")
async def get_getClubTournament(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: ClubTournamentWhereUniqueInput!) {
      getClubTournament(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("getClubTournament", {})

@mcp.resource("footium://getCompetition/{where}")
async def get_getCompetition(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: CompetitionWhereUniqueInput!) {
      getCompetition(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("getCompetition", {})

@mcp.resource("footium://getConfigValues/{keys}")
async def get_getConfigValues(keys: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($keys: [String!]!) {
      getConfigValues(keys: $keys) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "keys": keys,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("getConfigValues", {})

@mcp.resource("footium://getDivision/{where}")
async def get_getDivision(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: DivisionWhereUniqueInput!) {
      getDivision(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("getDivision", {})

@mcp.resource("footium://getFixture/{where}")
async def get_getFixture(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: FixtureWhereUniqueInput!) {
      getFixture(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("getFixture", {})

@mcp.resource("footium://getFormation/{where}")
async def get_getFormation(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: FormationWhereUniqueInput!) {
      getFormation(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("getFormation", {})

@mcp.resource("footium://getFormationSlot/{where}")
async def get_getFormationSlot(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: FormationSlotWhereUniqueInput!) {
      getFormationSlot(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("getFormationSlot", {})

@mcp.resource("footium://getKit/{where}")
async def get_getKit(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: KitWhereUniqueInput!) {
      getKit(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("getKit", {})

@mcp.resource("footium://getLineup/{where}")
async def get_getLineup(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: LineupWhereUniqueInput!) {
      getLineup(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("getLineup", {})

@mcp.resource("footium://getMatch/{where}")
async def get_getMatch(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: MatchWhereUniqueInput!) {
      getMatch(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("getMatch", {})

@mcp.resource("footium://getMatchChange/{where}")
async def get_getMatchChange(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: MatchChangeWhereUniqueInput!) {
      getMatchChange(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("getMatchChange", {})

@mcp.resource("footium://getMatchConfiguration/{where}")
async def get_getMatchConfiguration(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: MatchConfigurationWhereUniqueInput!) {
      getMatchConfiguration(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("getMatchConfiguration", {})

@mcp.resource("footium://getMerkleRoot/{where}")
async def get_getMerkleRoot(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: MerkleRootWhereUniqueInput!) {
      getMerkleRoot(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("getMerkleRoot", {})

@mcp.resource("footium://getNextRegistrationWindowUpdate")
async def get_getNextRegistrationWindowUpdate() -> Dict[str, Any]:
    """None"""
    query = """
    query {
      getNextRegistrationWindowUpdate {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    result = await client.execute(query)
    return result.get("data", {}).get("getNextRegistrationWindowUpdate", {})

@mcp.resource("footium://getOwner/{where}")
async def get_getOwner(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: OwnerWhereUniqueInput!) {
      getOwner(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("getOwner", {})

@mcp.resource("footium://getPlayer/{where}")
async def get_getPlayer(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PlayerWhereUniqueInput!) {
      getPlayer(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("getPlayer", {})

@mcp.resource("footium://getPlayerLineup/{where}")
async def get_getPlayerLineup(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PlayerLineupWhereUniqueInput!) {
      getPlayerLineup(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("getPlayerLineup", {})

@mcp.resource("footium://getPlayerRegistration/{where}")
async def get_getPlayerRegistration(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PlayerRegistrationWhereUniqueInput!) {
      getPlayerRegistration(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("getPlayerRegistration", {})

@mcp.resource("footium://getPositionalRating/{where}")
async def get_getPositionalRating(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PositionalRatingWhereUniqueInput!) {
      getPositionalRating(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("getPositionalRating", {})

@mcp.resource("footium://getPrizeAssignment/{where}")
async def get_getPrizeAssignment(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PrizeAssignmentWhereUniqueInput!) {
      getPrizeAssignment(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("getPrizeAssignment", {})

@mcp.resource("footium://getPromotionSelector/{where}")
async def get_getPromotionSelector(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PromotionSelectorWhereUniqueInput!) {
      getPromotionSelector(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("getPromotionSelector", {})

@mcp.resource("footium://getRegistrationWindow/{where}")
async def get_getRegistrationWindow(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: RegistrationWindowWhereUniqueInput!) {
      getRegistrationWindow(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("getRegistrationWindow", {})

@mcp.resource("footium://getSeason/{where}")
async def get_getSeason(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: SeasonWhereUniqueInput!) {
      getSeason(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("getSeason", {})

@mcp.resource("footium://getStadium/{where}")
async def get_getStadium(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: StadiumWhereUniqueInput!) {
      getStadium(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("getStadium", {})

@mcp.resource("footium://getStadiumStand/{where}")
async def get_getStadiumStand(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: StadiumStandWhereUniqueInput!) {
      getStadiumStand(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("getStadiumStand", {})

@mcp.resource("footium://getTournament/{where}")
async def get_getTournament(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: TournamentWhereUniqueInput!) {
      getTournament(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("getTournament", {})

@mcp.resource("footium://getTournamentResult/{where}")
async def get_getTournamentResult(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: TournamentResultWhereUniqueInput!) {
      getTournamentResult(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("getTournamentResult", {})

@mcp.resource("footium://getTrainingSlot/{where}")
async def get_getTrainingSlot(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: TrainingSlotWhereUniqueInput!) {
      getTrainingSlot(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("getTrainingSlot", {})

@mcp.resource("footium://isRegistrationWindowOpen")
async def get_isRegistrationWindowOpen() -> Dict[str, Any]:
    """None"""
    query = """
    query {
      isRegistrationWindowOpen {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    result = await client.execute(query)
    return result.get("data", {}).get("isRegistrationWindowOpen", {})

@mcp.resource("footium://kit/{where}")
async def get_kit(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: KitWhereUniqueInput!) {
      kit(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("kit", {})

@mcp.resource("footium://kits/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_kits(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: KitWhereInput, $orderBy: [KitOrderByWithRelationInput!], $cursor: KitWhereUniqueInput, $take: Int, $skip: Int, $distinct: [KitScalarFieldEnum!]) {
      kits(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("kits", {})

@mcp.resource("footium://leaguePromotionRelegation")
async def get_leaguePromotionRelegation() -> Dict[str, Any]:
    """None"""
    query = """
    query {
      leaguePromotionRelegation {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    result = await client.execute(query)
    return result.get("data", {}).get("leaguePromotionRelegation", {})

@mcp.resource("footium://lineup/{where}")
async def get_lineup(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: LineupWhereUniqueInput!) {
      lineup(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("lineup", {})

@mcp.resource("footium://lineups/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_lineups(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: LineupWhereInput, $orderBy: [LineupOrderByWithRelationInput!], $cursor: LineupWhereUniqueInput, $take: Int, $skip: Int, $distinct: [LineupScalarFieldEnum!]) {
      lineups(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("lineups", {})

@mcp.resource("footium://match/{where}")
async def get_match(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: MatchWhereUniqueInput!) {
      match(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("match", {})

@mcp.resource("footium://matchChange/{where}")
async def get_matchChange(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: MatchChangeWhereUniqueInput!) {
      matchChange(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("matchChange", {})

@mcp.resource("footium://matchChanges/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_matchChanges(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: MatchChangeWhereInput, $orderBy: [MatchChangeOrderByWithRelationInput!], $cursor: MatchChangeWhereUniqueInput, $take: Int, $skip: Int, $distinct: [MatchChangeScalarFieldEnum!]) {
      matchChanges(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("matchChanges", {})

@mcp.resource("footium://matchConfiguration/{where}")
async def get_matchConfiguration(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: MatchConfigurationWhereUniqueInput!) {
      matchConfiguration(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("matchConfiguration", {})

@mcp.resource("footium://matchConfigurations/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_matchConfigurations(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: MatchConfigurationWhereInput, $orderBy: [MatchConfigurationOrderByWithRelationInput!], $cursor: MatchConfigurationWhereUniqueInput, $take: Int, $skip: Int, $distinct: [MatchConfigurationScalarFieldEnum!]) {
      matchConfigurations(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("matchConfigurations", {})

@mcp.resource("footium://merkleRoot/{where}")
async def get_merkleRoot(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: MerkleRootWhereUniqueInput!) {
      merkleRoot(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("merkleRoot", {})

@mcp.resource("footium://merkleRoots/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_merkleRoots(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: MerkleRootWhereInput, $orderBy: [MerkleRootOrderByWithRelationInput!], $cursor: MerkleRootWhereUniqueInput, $take: Int, $skip: Int, $distinct: [MerkleRootScalarFieldEnum!]) {
      merkleRoots(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("merkleRoots", {})

@mcp.resource("footium://owner/{where}")
async def get_owner(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: OwnerWhereUniqueInput!) {
      owner(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("owner", {})

@mcp.resource("footium://owners/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_owners(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: OwnerWhereInput, $orderBy: [OwnerOrderByWithRelationInput!], $cursor: OwnerWhereUniqueInput, $take: Int, $skip: Int, $distinct: [OwnerScalarFieldEnum!]) {
      owners(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("owners", {})

@mcp.resource("footium://player/{where}")
async def get_player(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PlayerWhereUniqueInput!) {
      player(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("player", {})

@mcp.resource("footium://playerLineup/{where}")
async def get_playerLineup(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PlayerLineupWhereUniqueInput!) {
      playerLineup(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("playerLineup", {})

@mcp.resource("footium://playerLineups/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_playerLineups(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PlayerLineupWhereInput, $orderBy: [PlayerLineupOrderByWithRelationInput!], $cursor: PlayerLineupWhereUniqueInput, $take: Int, $skip: Int, $distinct: [PlayerLineupScalarFieldEnum!]) {
      playerLineups(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("playerLineups", {})

@mcp.resource("footium://playerRegistration/{where}")
async def get_playerRegistration(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PlayerRegistrationWhereUniqueInput!) {
      playerRegistration(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("playerRegistration", {})

@mcp.resource("footium://playerRegistrations/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_playerRegistrations(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PlayerRegistrationWhereInput, $orderBy: [PlayerRegistrationOrderByWithRelationInput!], $cursor: PlayerRegistrationWhereUniqueInput, $take: Int, $skip: Int, $distinct: [PlayerRegistrationScalarFieldEnum!]) {
      playerRegistrations(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("playerRegistrations", {})

@mcp.resource("footium://players/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_players(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PlayerWhereInput, $orderBy: [PlayerOrderByWithRelationInput!], $cursor: PlayerWhereUniqueInput, $take: Int, $skip: Int, $distinct: [PlayerScalarFieldEnum!]) {
      players(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("players", {})

@mcp.resource("footium://positionalRating/{where}")
async def get_positionalRating(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PositionalRatingWhereUniqueInput!) {
      positionalRating(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("positionalRating", {})

@mcp.resource("footium://positionalRatings/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_positionalRatings(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PositionalRatingWhereInput, $orderBy: [PositionalRatingOrderByWithRelationInput!], $cursor: PositionalRatingWhereUniqueInput, $take: Int, $skip: Int, $distinct: [PositionalRatingScalarFieldEnum!]) {
      positionalRatings(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("positionalRatings", {})

@mcp.resource("footium://prize/{where}")
async def get_prize(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PrizeWhereUniqueInput!) {
      prize(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("prize", {})

@mcp.resource("footium://prizeAssignment/{where}")
async def get_prizeAssignment(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PrizeAssignmentWhereUniqueInput!) {
      prizeAssignment(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("prizeAssignment", {})

@mcp.resource("footium://prizeAssignments/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_prizeAssignments(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PrizeAssignmentWhereInput, $orderBy: [PrizeAssignmentOrderByWithRelationInput!], $cursor: PrizeAssignmentWhereUniqueInput, $take: Int, $skip: Int, $distinct: [PrizeAssignmentScalarFieldEnum!]) {
      prizeAssignments(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("prizeAssignments", {})

@mcp.resource("footium://prizeClaim/{where}")
async def get_prizeClaim(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PrizeClaimWhereUniqueInput!) {
      prizeClaim(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("prizeClaim", {})

@mcp.resource("footium://prizeClaimMerkleProof/{prizeClaimId}")
async def get_prizeClaimMerkleProof(prizeClaimId: float) -> Dict[str, Any]:
    """None"""
    query = """
    query($prizeClaimId: Float!) {
      prizeClaimMerkleProof(prizeClaimId: $prizeClaimId) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "prizeClaimId": prizeClaimId,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("prizeClaimMerkleProof", {})

@mcp.resource("footium://prizeClaimMerkleRoot/{contractAddress}")
async def get_prizeClaimMerkleRoot(contractAddress: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($contractAddress: String!) {
      prizeClaimMerkleRoot(contractAddress: $contractAddress) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "contractAddress": contractAddress,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("prizeClaimMerkleRoot", {})

@mcp.resource("footium://prizeClaimMerkleRootToCommit/{regenerate}/{contractAddress}")
async def get_prizeClaimMerkleRootToCommit(regenerate: bool, contractAddress: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($regenerate: Boolean, $contractAddress: String!) {
      prizeClaimMerkleRootToCommit(regenerate: $regenerate, contractAddress: $contractAddress) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "regenerate": regenerate,
        "contractAddress": contractAddress,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("prizeClaimMerkleRootToCommit", {})

@mcp.resource("footium://prizeClaims/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_prizeClaims(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PrizeClaimWhereInput, $orderBy: [PrizeClaimOrderByWithRelationInput!], $cursor: PrizeClaimWhereUniqueInput, $take: Int, $skip: Int, $distinct: [PrizeClaimScalarFieldEnum!]) {
      prizeClaims(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("prizeClaims", {})

@mcp.resource("footium://prizeValue/{where}")
async def get_prizeValue(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PrizeValueWhereUniqueInput!) {
      prizeValue(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("prizeValue", {})

@mcp.resource("footium://prizeValues/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_prizeValues(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PrizeValueWhereInput, $orderBy: [PrizeValueOrderByWithRelationInput!], $cursor: PrizeValueWhereUniqueInput, $take: Int, $skip: Int, $distinct: [PrizeValueScalarFieldEnum!]) {
      prizeValues(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("prizeValues", {})

@mcp.resource("footium://prizes/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_prizes(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PrizeWhereInput, $orderBy: [PrizeOrderByWithRelationInput!], $cursor: PrizeWhereUniqueInput, $take: Int, $skip: Int, $distinct: [PrizeScalarFieldEnum!]) {
      prizes(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("prizes", {})

@mcp.resource("footium://promotionSelector/{where}")
async def get_promotionSelector(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PromotionSelectorWhereUniqueInput!) {
      promotionSelector(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("promotionSelector", {})

@mcp.resource("footium://promotionSelectors/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_promotionSelectors(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: PromotionSelectorWhereInput, $orderBy: [PromotionSelectorOrderByWithRelationInput!], $cursor: PromotionSelectorWhereUniqueInput, $take: Int, $skip: Int, $distinct: [PromotionSelectorScalarFieldEnum!]) {
      promotionSelectors(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("promotionSelectors", {})

@mcp.resource("footium://registrationWindow/{where}")
async def get_registrationWindow(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: RegistrationWindowWhereUniqueInput!) {
      registrationWindow(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("registrationWindow", {})

@mcp.resource("footium://registrationWindows/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_registrationWindows(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: RegistrationWindowWhereInput, $orderBy: [RegistrationWindowOrderByWithRelationInput!], $cursor: RegistrationWindowWhereUniqueInput, $take: Int, $skip: Int, $distinct: [RegistrationWindowScalarFieldEnum!]) {
      registrationWindows(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("registrationWindows", {})

@mcp.resource("footium://season/{where}")
async def get_season(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: SeasonWhereUniqueInput!) {
      season(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("season", {})

@mcp.resource("footium://seasons/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_seasons(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: SeasonWhereInput, $orderBy: [SeasonOrderByWithRelationInput!], $cursor: SeasonWhereUniqueInput, $take: Int, $skip: Int, $distinct: [SeasonScalarFieldEnum!]) {
      seasons(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("seasons", {})

@mcp.resource("footium://serverMetadata")
async def get_serverMetadata() -> Dict[str, Any]:
    """None"""
    query = """
    query {
      serverMetadata {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    result = await client.execute(query)
    return result.get("data", {}).get("serverMetadata", {})

@mcp.resource("footium://stadium/{where}")
async def get_stadium(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: StadiumWhereUniqueInput!) {
      stadium(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("stadium", {})

@mcp.resource("footium://stadiumStand/{where}")
async def get_stadiumStand(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: StadiumStandWhereUniqueInput!) {
      stadiumStand(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("stadiumStand", {})

@mcp.resource("footium://stadiumStands/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_stadiumStands(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: StadiumStandWhereInput, $orderBy: [StadiumStandOrderByWithRelationInput!], $cursor: StadiumStandWhereUniqueInput, $take: Int, $skip: Int, $distinct: [StadiumStandScalarFieldEnum!]) {
      stadiumStands(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("stadiumStands", {})

@mcp.resource("footium://stadiums/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_stadiums(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: StadiumWhereInput, $orderBy: [StadiumOrderByWithRelationInput!], $cursor: StadiumWhereUniqueInput, $take: Int, $skip: Int, $distinct: [StadiumScalarFieldEnum!]) {
      stadiums(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("stadiums", {})

@mcp.resource("footium://structuredPrizes/{competitionName}/{seasonId}")
async def get_structuredPrizes(competitionName: str, seasonId: float) -> Dict[str, Any]:
    """None"""
    query = """
    query($competitionName: String!, $seasonId: Float!) {
      structuredPrizes(competitionName: $competitionName, seasonId: $seasonId) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "competitionName": competitionName,
        "seasonId": seasonId,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("structuredPrizes", {})

@mcp.resource("footium://totalClaimValue/{contractAddress}/{ownerId}")
async def get_totalClaimValue(contractAddress: str, ownerId: float) -> Dict[str, Any]:
    """None"""
    query = """
    query($contractAddress: String!, $ownerId: Float!) {
      totalClaimValue(contractAddress: $contractAddress, ownerId: $ownerId) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "contractAddress": contractAddress,
        "ownerId": ownerId,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("totalClaimValue", {})

@mcp.resource("footium://tournament/{where}")
async def get_tournament(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: TournamentWhereUniqueInput!) {
      tournament(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("tournament", {})

@mcp.resource("footium://tournamentResult/{where}")
async def get_tournamentResult(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: TournamentResultWhereUniqueInput!) {
      tournamentResult(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("tournamentResult", {})

@mcp.resource("footium://tournamentResults/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_tournamentResults(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: TournamentResultWhereInput, $orderBy: [TournamentResultOrderByWithRelationInput!], $cursor: TournamentResultWhereUniqueInput, $take: Int, $skip: Int, $distinct: [TournamentResultScalarFieldEnum!]) {
      tournamentResults(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("tournamentResults", {})

@mcp.resource("footium://tournaments/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_tournaments(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: TournamentWhereInput, $orderBy: [TournamentOrderByWithRelationInput!], $cursor: TournamentWhereUniqueInput, $take: Int, $skip: Int, $distinct: [TournamentScalarFieldEnum!]) {
      tournaments(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("tournaments", {})

@mcp.resource("footium://trainingSlot/{where}")
async def get_trainingSlot(where: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: TrainingSlotWhereUniqueInput!) {
      trainingSlot(where: $where) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("trainingSlot", {})

@mcp.resource("footium://trainingSlots/{where}/{orderBy}/{cursor}/{take}/{skip}/{distinct}")
async def get_trainingSlots(where: str, orderBy: str, cursor: str, take: int, skip: int, distinct: str) -> Dict[str, Any]:
    """None"""
    query = """
    query($where: TrainingSlotWhereInput, $orderBy: [TrainingSlotOrderByWithRelationInput!], $cursor: TrainingSlotWhereUniqueInput, $take: Int, $skip: Int, $distinct: [TrainingSlotScalarFieldEnum!]) {
      trainingSlots(where: $where, orderBy: $orderBy, cursor: $cursor, take: $take, skip: $skip, distinct: $distinct) {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    variables = {
        "where": where,
        "orderBy": orderBy,
        "cursor": cursor,
        "take": take,
        "skip": skip,
        "distinct": distinct,
    }
    result = await client.execute(query, variables)
    return result.get("data", {}).get("trainingSlots", {})

@mcp.resource("footium://unregistrationLimit")
async def get_unregistrationLimit() -> Dict[str, Any]:
    """None"""
    query = """
    query {
      unregistrationLimit {
        # Add fields here based on the schema
        id
        name
      }
    }
    """
    result = await client.execute(query)
    return result.get("data", {}).get("unregistrationLimit", {})
