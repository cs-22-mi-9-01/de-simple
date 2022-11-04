# Source: https://pythonspeed.com/articles/activate-conda-dockerfile/#working

FROM continuumio/anaconda3

WORKDIR /app

# Create the environment:
COPY environment.yml .
RUN conda env create -f environment.yml

# Copy code:
COPY de-simple .

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "tkgc", "/bin/bash", "-c"]

# The code to run when the image is being created - Learning the model is part of the docker image creation
#RUN python main.py -dropout 0.4 -se_prop 0.68 -model DE_TransE



############# HOW TO BUILD AND RUN #############

# Create docker image from docker file:
#docker build --tag=tkgc .

# Run docker container and use the command prompt in the container
#docker run --gpus=all -it --name=de tkgc bash

# Activate conda env in container and run:
#conda activate tkgc && python main.py -dropout 0.4 -se_prop 0.68 -model DE_TransE -ne 4 -neg_ratio 2 -save_each 2

# To copy the models out of the container:
#docker cp de:/app/models ./models