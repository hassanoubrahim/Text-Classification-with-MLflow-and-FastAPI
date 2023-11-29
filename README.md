# Text-Classification-with-MLflow-and-FastAPI
# Mlflow

This project demonstrates various steps in the machine learning workflow, including data preprocessing, model training, model tracking, serialization, creating REST APIs, containerization, and consumption.

## Project Overview

- Start by preprocessing your data.
- Train 5 ML models.
- Try to track model performance, versions, and parameters using MLflow. ![Image Description](https://media.discordapp.net/attachments/1179056718064386200/1179056738197049354/image.png?ex=65786528&is=6565f028&hm=6af80c7ef9f366517c3d85cb9216725e799fe46700f27549aceff58bacb18310&=&format=webp&width=947&height=499)
in our case it is very that the 3rd model(Logistic Regression) perform better with an accuracy of 0.90, therefore we will use for the rest of this lab
- Save your best model in ONNX format and its dedicated preprocessing transformations in pickle format (i.e., using transformers API).

## Usage

### Using FastAPI

- Create a REST API for your model.
- Using the serialized files.
- Package your model as a container using Docker.
- Consume your created APIs using Curl.

### Using Flask

- Create a dedicated application to consume your API.
- Package your application as a container using Docker.

## How to Run

[Add instructions on how to run your project here.]

## Screenshots

[Add screenshots or diagrams here to visualize your project, if applicable.]

## Dependencies

[Include a list of dependencies or prerequisites for running your project.]

## License

This project is licensed under the [License Name] - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

[Add acknowledgments or credits for libraries, tutorials, or other resources you used.]

## Contact

[Provide your contact information for inquiries or collaboration.]

