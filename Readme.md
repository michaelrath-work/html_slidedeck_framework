# Flexible reveal.js workflow

Key features

* Design each slide on its own, in a separate file, e.g. [slides/slide1.html](slides/slide1.html))
* On easy to comprehend slide [master](templates/master.html)
* Build everything with a [bash script](build.sh) using [mo](https://github.com/tests-always-included/mo)
    * The slide ordering can easily be changed
    * Slides could be removed etc
    * No need to deal with one big messy HTML file
* install `mo`
    ```bash
    curl -sSL https://git.io/get-mo -o ./mo.sh
    chmod 755 ./mo.sh
    ```
