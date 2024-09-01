provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"  # Ganti dengan AMI ID yang sesuai
  instance_type = "t2.micro"

  tags = {
    Name = "example-instance"
  }
}
