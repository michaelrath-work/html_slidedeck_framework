from jinja2 import Environment, FileSystemLoader, select_autoescape


def main():
    env = Environment(
        loader=FileSystemLoader('templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('master.html')

    # easily decide, what goes into the slide deck and in what order
    slides = [
        'slides/slide2.html',
        'slides/slide1.html',
        # 'slides/slide2.html',
        ]

    with open('presentation.html', 'w') as fp:
        fp.write(template.render(slides=slides))

if __name__ == '__main__':
    main()
