import json
from flask import Flask
from flask import request
import GraphAlgorithms
import Validation

app = Flask(__name__)

class MazeSolutionResult:
    def __init__(self, is_success, input_data, solution, response_message):
        self.input = None
        self.solution = None
        self.length = None
        if is_success:
            self.status = response_message
        else:
            self.error = response_message
        if input_data is not None:
            self.input = str(input_data)
        if solution is not None:
            self.solution = solution
        if solution is not None:
            self.length = len(solution)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return "Welcome!"
    else:
        json_data = request.data
        validation_result = Validation.validate_and_build_graph_data(json_data)
        result = None
        if validation_result.is_success:
            bfs_result = GraphAlgorithms.bfs_shortest_path(validation_result.graph, validation_result.source, validation_result.destination)
            if bfs_result.is_success:
                result = MazeSolutionResult(True, validation_result.graph, bfs_result.path_array, "OK")
            else:
                result = MazeSolutionResult(True, validation_result.graph, None, "No solution found")
        else:
            result = MazeSolutionResult(False, None, None, validation_result.error_message)
        return json.dumps(result.__dict__), 200, {'Content-Type': 'application/json; charset=utf-8'}

if __name__ == "__main__":
    app.run()
