from fastmcp import FastMCP
import ipaddress

mcp = FastMCP("Subnet Calculator MCP Server")

@mcp.tool()
def calculate_subnet(cidr: str) -> dict:
    """
    Calculate subnet details for a given CIDR (e.g., '192.168.1.0/24').
    Returns network address, broadcast address, usable host range, and number of hosts.
    """
    try:
        net = ipaddress.ip_network(cidr, strict=False)
        hosts = list(net.hosts())
        return {
            "network_address": str(net.network_address),
            "broadcast_address": str(net.broadcast_address),
            "netmask": str(net.netmask),
            "wildcard_mask": str(net.hostmask),
            "usable_host_range": f"{hosts[0]} - {hosts[-1]}" if hosts else "N/A",
            "number_of_usable_hosts": len(hosts)
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    mcp.run(transport="sse")
