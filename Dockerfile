#  NAME:  SHAKHRIZOD
#  FILE:  Main dockerfile - Docker
#  REQUIREMENTS:  Docker


#  Using basic python
FROM python:3.10-slim

# Copying files to container
WORKDIR /app
COPY . .

#  Add requirements
RUN pip install -r requirements.txt

#  Add default command
CMD ["python", "src/main.py"]
