**Update DNS Records with Reg.RU**

A Python script that updates or sets A records for the specified domain at Reg.RU.

### Table of Contents

* [Usage](#usage)
* [Installation](#installation)
* [Building Docker Container](#building-docker-container)
* [Running Docker Container](#running-docker-container)
* [Environment Variables](#environment-variables)

## Usage

This script updates or sets A records for the specified domain at Reg.RU. It requires three environment variables to be set:

* `REG_RU_USERNAME`: Your Reg.RU username
* `REG_RU_PASSWORD`: Your Reg.RU password
* `DOMAIN_NAME`: The name of the domain you want to update

Typical usage as analog of DDNS service. Just implement it into your router or server behind NAT and use cronjobs to handle it.

## Installation

To install this script, run the following commands:
```bash
git clone https://github.com/usrdmn/update-dns-record-reg-ru.git
cd update_dns
pip install -r requirements.txt
```

## Building Docker Container

To build a Docker container for this script, run the following commands:
```bash
docker build -t update-dns .
```
This will create an image with the tag `update-dns`.

## Running Docker Container

To run the Docker container, use:
```bash
docker run update-dns
```
This will start a new container based on the `update-dns` image and map port 80 from the container to port 80 on your host machine.

## Environment Variables

The following environment variables need to be set:

* `REG_RU_USERNAME`: Your Reg.RU username
* `REG_RU_PASSWORD`: Your Reg.RU password
* `DOMAIN_NAME`: The name of the domain you want to update

You can set these environment variables in the Docker container using:
```bash
docker run -e REG_RU_USERNAME=your-username -e REG_RU_PASSWORD=your-password -e DOMAIN_NAME=example.com update-dns
```
Make sure to replace `your-username`, `your-password`, and `example.com` with your actual values.

### Contributing

Contributions are welcome! If you'd like to contribute, please fork this repository and submit a pull request.