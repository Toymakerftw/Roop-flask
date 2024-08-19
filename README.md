# Roop-flask

Roop-flask is a Flask web application that allows you to swap faces in videos using the Roop deep learning model. It is a fork of [s0md3v's roop](https://github.com/s0md3v/roop).

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Toymakerftw/Roop-flask.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Roop-flask
    ```

3. Build the Docker image:

    ```bash
    docker build -t roop-flask .
    ```

4. Run the Docker container:

    ```bash
docker run -p 7777:7777 roop-flask
    ```

5. Open your web browser and navigate to `http://localhost:4000` to see the Roop-flask web application running.

## Contributing

If you'd like to contribute to this project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with a clear and concise commit message.
4. Push your changes to your fork.
5. Submit a pull request to the main repository.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
