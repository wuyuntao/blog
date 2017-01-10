from error import optimal
---------------------

Initialize blog with pelican
---------------------

* Create a virtualenv.
* Install everything in `requirements.txt`.
* Setup your `.gitignore` file.
* Run `pelican-quickstart`.
* Create a `plugins` folder.
* Run `git init`.
* Run `git submodule add git://github.com/danielfrg/pelican-ipynb.git plugins/ipynb`.
* Create any notebooks you want in the `content` folder.
    * Remember to create corresponding `.ipynb-meta` files.
* Edit pelicanconf.py to the lines that activate the `pelican-ipynb` plugin.
* Run `pelican content`.
* Switch to the `output` directory and run `python -m pelican.server`.

Publish post to blog
---------------------

* Run `make github` to publish content to `github`
