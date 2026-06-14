from __future__ import annotations

import uvicorn
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "inventory-server",
    host="127.0.0.1",
    port=8001,
    streamable_http_path="/mcp",
    stateless_http=True,
)


@mcp.tool()
def get_inventory_status(item_id: str) -> str:
    """
    Look up inventory status for one item.
    """
    return f"Inventory status for {item_id}: placeholder result"


@mcp.tool()
def explain_table(table_name: str) -> str:
    """
    Return metadata or explanation for a warehouse table.
    """
    return f"{table_name} is a warehouse table used in BI ETL."


if __name__ == "__main__":
    print("=" * 60)
    print("Inventory MCP Server Starting")
    print("=" * 60)
    print("Tools exposed:")
    print("  - get_inventory_status")
    print("  - explain_table")
    print()
    print("Transport: streamable-http")
    print(f"MCP URL: http://{mcp.settings.host}:{mcp.settings.port}{mcp.settings.streamable_http_path}")
    print("=" * 60)

    app = mcp.streamable_http_app()

    uvicorn.run(
        app,
        host=mcp.settings.host,
        port=mcp.settings.port,
        log_level="info",
    )