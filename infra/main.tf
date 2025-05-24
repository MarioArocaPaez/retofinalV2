terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_network" "reto_network" {
  name = "reto-network"
}

resource "docker_container" "reto_container" {
  image = var.docker_image
  name  = "reto-final-container"
  ports {
    internal = 80
    external = 5000
  }
  networks_advanced {
    name = docker_network.reto_network.name
  }
}
