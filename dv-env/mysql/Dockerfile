#FROM mysql

#修正9/22
ARG MYSQL_VERSION=8
FROM mysql:8.0-debian

COPY my.cnf /etc/mysql/conf.d/my.cnf

#ポートを開ける
EXPOSE 3306

# コンテナ内で日本語が打てるようにlocalを変更といらないファイル削除
RUN apt-get update && apt-get install -y locales \
    && sed -i -e 's/# ja_JP.UTF-8 UTF-8/ja_JP.UTF-8 UTF-8/' /etc/locale.gen \
    && locale-gen ja_JP.UTF-8

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8

#MySQL設定ファイルをイメージ内にコピー
ADD ./my.cnf /etc/mysql/conf.d/my.cnf

#docker runに実行される
CMD ["mysqld"]