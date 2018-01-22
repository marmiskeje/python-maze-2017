import json

class InputValidationResult:
    def __init__(self, is_success, error_message, graph, source, destination):
        self.is_success = is_success
        self.error_message = error_message
        self.graph = graph
        self.source = source
        self.destination = destination

def validate_and_build_graph_data(json_data):
    is_success = False
    error_message = None
    graph = None
    source = None
    destination = None
    try:
        input_data = json.loads(json_data)
        graph = dict()
        source = input_data["start"]
        destination = input_data["end"]
        for vertex in input_data["rooms"]:
            if vertex in graph:
                error_message = "Invalid input - multiple rooms with the same name"
                break
            else:
                graph[vertex] = set()
        # vertices validation
        if error_message is None:
            if len(graph) == 0:
                graph = None
                error_message = "Invalid input - No rooms"
            elif source not in graph:
                source = None
                error_message = "Invalid input - Start is not a room"
            elif destination not in graph:
                destination = None
                error_message = "Invalid input - End is not a room"
        # edges validation
        if error_message is None:
            for edge in input_data["corridors"]:
                if edge[0] in graph and edge[1] in graph and edge[0] != edge[1]:
                    graph[edge[0]].add(edge[1])
                    graph[edge[1]].add(edge[0])
                else:
                    error_message = "Invalid input - wrong corridor " + edge[0] + " -> " + edge[1]
                    break
    except Exception:
        error_message = "Invalid json data"
    is_success = error_message is None and graph is not None and source is not None and destination is not None
    if not is_success and error_message is None:
        error_message = "Invalid input"
    return InputValidationResult(is_success, error_message, graph, source, destination)