# Flexible reveal.js workflow

Key features

* Design each slide on its own, in a separate file, e.g. [templates/slides/slide1.html](templates/slides/slide1.html))
* On easy to comprehend slide [master](templates/master.html)
* Build everything with a [python script](build.py) using [jinja](http://jinja.pocoo.org)
    * The slide ordering can easily be changed
    * Slides could be removed etc
    * No need to deal with one big messy HTML file
