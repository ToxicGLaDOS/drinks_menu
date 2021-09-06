FROM arm32v7/python

# Don't forget to set the SECRET_KEY environment variable
# --env SECRET_KEY=<key> on command line

RUN pip install django django_measurement uwsgi psycopg2 Pillow
RUN groupadd -g 2003 drink-menu
RUN useradd -u 2003 -g 2003 drink-menu

RUN rm -rf /root/.cache
RUN mkdir /menu
RUN chown drink-menu:drink-menu /menu

COPY --chown=drink-menu:drink-menu menu /menu/menu
COPY --chown=drink-menu:drink-menu drinks_menu /menu/drinks_menu
COPY --chown=drink-menu:drink-menu manage.py /menu/

USER drink-menu
WORKDIR /menu
ENTRYPOINT ["uwsgi", "--http", ":8080", "--module", "menu.wsgi"]
