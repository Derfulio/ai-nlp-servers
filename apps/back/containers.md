# Why containers?
Voir ***https://en.wikipedia.org/wiki/Docker_(software)***
## Bénéfices
- Plus rapides que les VMs (Less Overhead)
- Facile à reproduire (Reproducibility)
- Ne change pas (Immutable)

## Liste des fournisseurs de conteneurs
- Linux Containers:
  - LXC
  - LXD
  - CGManager
- Docker
- Windows Server

## Sample

### Exemple Dockerfile
1. FROM ubuntu:18.04 #Start from this base image
2. RUN apt-get update && apt-get install -y python3 #Update repository, then install python 3
3. RUN mkdir /aspen #Make dir aspen off the root
4. COPY test.py /aspen/test.py #Copy a file from outside the container into the aspen folder
5. RUN chmod a+rwx -R /aspen/ #Allow read write and execute in the aspen folder
6. ENTRYPOINT["aspen/test.py"] #When the container is run, start by this python script

### Docker Command Line
- To build the image: docker build -t [image name]
- To show images: docker Images
- To run an image: docker run [image name]