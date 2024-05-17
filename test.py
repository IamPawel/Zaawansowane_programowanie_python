from flask import Flask, send_file, make_response
import io
import base64

app = Flask(__name__)


@app.route("/download", methods=["GET"])
def download_file():
    # Przykładowe dane pliku
    file_data = "Hello, World!"

    # Konwersja danych na base64
    base64_data = base64.b64encode(file_data.encode()).decode()

    # Dekodowanie base64 do binarnego pliku
    decoded_file_data = base64.b64decode(base64_data)

    # Użycie io.BytesIO do stworzenia obiektu pliku w pamięci
    file_stream = io.BytesIO(decoded_file_data)

    # Tworzenie odpowiedzi, aby przeglądarka pobrała plik
    response = make_response(
        send_file(file_stream, as_attachment=True, download_name="example.txt")
    )
    response.headers["Content-Disposition"] = "attachment; filename=example.txt"
    response.mimetype = "text/plain"

    return response


if __name__ == "__main__":
    app.run(debug=True)
