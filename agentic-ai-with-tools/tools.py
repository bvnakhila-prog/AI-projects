from langchain_core.tools import tool

@tool # this decorator converts python functions to structured langchain basrtool
def calculator(expression: str) -> str:
    """Useful for evaluating mathematical expressions. Input must be a valid mathematical string. e.g., '2 + 2' or '15 * 45' . """
    try:
        #safely evaluate mathematical expressions
        result = eval(expression, {"__builtime__": None}, {})
        return f"Calculation Result : {result}"
    except Exception as e:
        return f"Error evaluating expression: {e}"

@tool
def get_system_status(service_name: str) -> str:
    """Retrieves the operational status of a company system or service (e.g., 'auth','database','billing')."""
    mock_db = {
        "auth" : "Operational (99.9% uptime)",
        "database" : "Degraded Performance (High latency on read operations)",
        "billing" : "Operational",
    }
    status = mock_db.get(service_name.lower(), " Unknown Service")
    return f"Status for '{service_name}' : {status}"