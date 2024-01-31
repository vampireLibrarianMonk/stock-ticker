# Use Red Hat UBI 8.8 as the base image
FROM registry.access.redhat.com/ubi8/ubi:8.8

# Install necessary packages
RUN yum install -y wget bzip2

# Install Micromamba
ENV MAMBA_ROOT_PREFIX=/opt/micromamba
RUN curl -Ls https://micro.mamba.pm/api/micromamba/linux-64/latest | tar -xvj bin/micromamba && \
    mkdir -p /opt/micromamba && \
    ./bin/micromamba shell init -s bash -p /opt/micromamba

# Copy relevant project files
RUN mkdir -p /home/user/stock-ticker
COPY environment.yml /home/user/stock-ticker/environment.yml
COPY stocks /home/user/stock-ticker/stocks

# Create the Conda environment using Micromamba
RUN micromamba create -f /home/user/stock-ticker/environment.yml && \
    micromamba clean --all --yes

# Set the working directory
WORKDIR /home/user/stock-ticker

# Activate the conda environment and start the application
ENTRYPOINT [ "/bin/bash", "-c", "micromamba run -n $(head -1 /home/user/stock-ticker/environment.yml | cut -d' ' -f2) /home/user/stock-ticker/stocks/manage.py runserver 0.0.0.0:8000" ]
