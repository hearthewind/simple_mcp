from mcp.server.fastmcp import FastMCP

mcp = FastMCP("inventory-server")

@mcp.tool()
def get_inventory_status(item_id: str) -> str:
    """
    Look up inventory status for one item.
    In real implementation, query SQL Server or an API here.
    """
    return f"Inventory status for {item_id}: placeholder result"

@mcp.tool()
def explain_table(table_name: str) -> str:
    """
    Return metadata or explanation for a warehouse table.
    """
    return f"{table_name} is a warehouse table used in BI ETL."

if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="127.0.0.1",
        port=8001,
        path="/mcp",
    )