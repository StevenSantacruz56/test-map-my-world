.PHONY: create_venv run_env deploy validate_pep8 build_image

# Target: create_venv
# Description: Installs the project dependencies using Poetry.
create_venv:
	@poetry env use 3.10
	@poetry install

# Target: run_env
# Description: Activates the virtual environment created by Poetry.
run_env:
	@poetry shell

# Target: run_env
# Description: Activates the virtual environment created by Poetry.
run_update_library:
	@poetry update

# Target: deploy
# Description: Runs the application using uvicorn with hot-reloading.
deploy: create_venv
	@uvicorn map_my_world.src.ports.rest.main:app --reload

# Target: validate_pep8
# Description: Validates the code style of the 'guarantee' module using flake8.
validate_pep8:
	@flake8 map_my_world --extend-exclude=dist,build --show-source --statistics

# Target: build_image
# Description: Builds a Docker image using the 'build_image.sh' script.
build_image:
	@sh $(CURDIR)/bash/build.sh $(NAME)

# Target: run_docker
# Description: Runs a Docker container using the 'localhost.yml' script in the 'devops' directory.
run_docker:
	@sh $(CURDIR)/bash/deploy_dev.sh

run_tests: run_tests
	@poetry run pytest --cov=map_my_world/core/services --cov-report=term-missing tests
