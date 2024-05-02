
1. **Full Installation of PostgreSQL**
   - Installs all necessary packages and dependencies for PostgreSQL.
   - Configures PostgreSQL with default settings.
   - Sets up PostgreSQL to listen on all network interfaces.
   - Configures PostgreSQL to allow password authentication for all users.
   - Restarts the PostgreSQL service.
   - Sets the password for the PostgreSQL user to 'postgres'.

2. **Health Check**
   - Checks the health of the PostgreSQL server by executing a simple query (`select 1;`).
   - Displays the result of the query.
   
****Example:****

➜  PostgresPro git:(main) ✗ python3 main.py localhost --port 75
/Users/antonsemenov/.ssh/id_rsa.pub
75
1 - full_install_psql
2 - health_check
Enter your choice: 1
1
Hit:1 http://ports.ubuntu.com/ubuntu-ports noble InRelease

Get:2 http://ports.ubuntu.com/ubuntu-ports noble-updates InRelease [89.7 kB]

Hit:3 http://ports.ubuntu.com/ubuntu-ports noble-backports InRelease

Hit:4 http://ports.ubuntu.com/ubuntu-ports noble-security InRelease

Get:5 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 Packages [24.0 kB]

Fetched 114 kB in 2s (52.0 kB/s)

Reading package lists...

Building dependency tree...

Reading state information...

All packages are up to date.

Reading package lists...

Building dependency tree...

Reading state information...

The following additional packages will be installed:

  libcommon-sense-perl libgdbm-compat4t64 libgdbm6t64 libjson-perl

  libjson-xs-perl libldap-common libldap2 libllvm17t64 libperl5.38t64 libpopt0

  libpq5 libsasl2-2 libsasl2-modules libsasl2-modules-db libsensors-config

  libsensors5 libtypes-serialiser-perl libxslt1.1 locales logrotate perl

  perl-modules-5.38 postgresql-client-16 postgresql-client-common

  postgresql-common ssl-cert sysstat xz-utils

Suggested packages:

  gdbm-l10n libsasl2-modules-gssapi-mit | libsasl2-modules-gssapi-heimdal

  libsasl2-modules-ldap libsasl2-modules-otp libsasl2-modules-sql lm-sensors

  bsd-mailx | mailx perl-doc libterm-readline-gnu-perl

  | libterm-readline-perl-perl make libtap-harness-archive-perl

  postgresql-doc-16 isag

The following NEW packages will be installed:

  libcommon-sense-perl libgdbm-compat4t64 libgdbm6t64 libjson-perl

  libjson-xs-perl libldap-common libldap2 libllvm17t64 libperl5.38t64 libpopt0

  libpq5 libsasl2-2 libsasl2-modules libsasl2-modules-db libsensors-config

  libsensors5 libtypes-serialiser-perl libxslt1.1 locales logrotate perl

  perl-modules-5.38 postgresql-16 postgresql-client-16

  postgresql-client-common postgresql-common ssl-cert sysstat xz-utils

0 upgraded, 29 newly installed, 0 to remove and 0 not upgraded.

Need to get 55.8 MB of archives.

After this operation, 249 MB of additional disk space will be used.

Get:1 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 perl-modules-5.38 all 5.38.2-3.2build2 [3110 kB]

Get:2 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libgdbm6t64 arm64 1.23-5.1build1 [34.4 kB]

Get:3 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libgdbm-compat4t64 arm64 1.23-5.1build1 [6578 B]

Get:4 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libperl5.38t64 arm64 5.38.2-3.2build2 [4774 kB]

Get:5 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 perl arm64 5.38.2-3.2build2 [231 kB]

Get:6 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libjson-perl all 4.10000-1 [81.9 kB]

Get:7 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 postgresql-client-common all 257build1 [36.3 kB]

Get:8 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 ssl-cert all 1.1.2ubuntu1 [17.8 kB]

Get:9 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 postgresql-common all 257build1 [161 kB]

Get:10 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libpopt0 arm64 1.19+dfsg-1build1 [28.4 kB]

Get:11 http://ports.ubuntu.com/ubuntu-ports noble-updates/main arm64 locales all 2.39-0ubuntu8.1 [4234 kB]

Get:12 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 logrotate arm64 3.21.0-2build1 [50.9 kB]

Get:13 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libsensors-config all 1:3.6.0-9build1 [5546 B]

Get:14 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libsensors5 arm64 1:3.6.0-9build1 [27.0 kB]

Get:15 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 xz-utils arm64 5.6.1+really5.4.5-1 [268 kB]

Get:16 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 sysstat arm64 12.6.1-2 [480 kB]

Get:17 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libcommon-sense-perl arm64 3.75-3build3 [20.4 kB]

Get:18 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libtypes-serialiser-perl all 1.01-1 [11.6 kB]

Get:19 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libjson-xs-perl arm64 4.030-2build3 [83.1 kB]

Get:20 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libldap-common all 2.6.7+dfsg-1~exp1ubuntu8 [31.4 kB]

Get:21 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libsasl2-modules-db arm64 2.1.28+dfsg1-5ubuntu3 [21.4 kB]

Get:22 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libsasl2-2 arm64 2.1.28+dfsg1-5ubuntu3 [54.7 kB]

Get:23 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libldap2 arm64 2.6.7+dfsg-1~exp1ubuntu8 [193 kB]

Get:24 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libllvm17t64 arm64 1:17.0.6-9ubuntu1 [25.0 MB]

Get:25 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libpq5 arm64 16.2-1ubuntu4 [137 kB]

Get:26 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libsasl2-modules arm64 2.1.28+dfsg1-5ubuntu3 [69.4 kB]

Get:27 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 libxslt1.1 arm64 1.1.39-0exp1build1 [166 kB]

Get:28 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 postgresql-client-16 arm64 16.2-1ubuntu4 [1261 kB]

Get:29 http://ports.ubuntu.com/ubuntu-ports noble/main arm64 postgresql-16 arm64 16.2-1ubuntu4 [15.2 MB]

Fetched 55.8 MB in 55s (1023 kB/s)

Selecting previously unselected package perl-modules-5.38.

(Reading database ... 11142 files and directories currently installed.)

Preparing to unpack .../00-perl-modules-5.38_5.38.2-3.2build2_all.deb ...

Unpacking perl-modules-5.38 (5.38.2-3.2build2) ...

Selecting previously unselected package libgdbm6t64:arm64.

Preparing to unpack .../01-libgdbm6t64_1.23-5.1build1_arm64.deb ...

Unpacking libgdbm6t64:arm64 (1.23-5.1build1) ...

Selecting previously unselected package libgdbm-compat4t64:arm64.

Preparing to unpack .../02-libgdbm-compat4t64_1.23-5.1build1_arm64.deb ...

Unpacking libgdbm-compat4t64:arm64 (1.23-5.1build1) ...

Selecting previously unselected package libperl5.38t64:arm64.

Preparing to unpack .../03-libperl5.38t64_5.38.2-3.2build2_arm64.deb ...

Unpacking libperl5.38t64:arm64 (5.38.2-3.2build2) ...

Selecting previously unselected package perl.

Preparing to unpack .../04-perl_5.38.2-3.2build2_arm64.deb ...

Unpacking perl (5.38.2-3.2build2) ...

Selecting previously unselected package libjson-perl.

Preparing to unpack .../05-libjson-perl_4.10000-1_all.deb ...

Unpacking libjson-perl (4.10000-1) ...

Selecting previously unselected package postgresql-client-common.

Preparing to unpack .../06-postgresql-client-common_257build1_all.deb ...

Unpacking postgresql-client-common (257build1) ...

Selecting previously unselected package ssl-cert.

Preparing to unpack .../07-ssl-cert_1.1.2ubuntu1_all.deb ...

Unpacking ssl-cert (1.1.2ubuntu1) ...

Selecting previously unselected package postgresql-common.

Preparing to unpack .../08-postgresql-common_257build1_all.deb ...

Adding 'diversion of /usr/bin/pg_config to /usr/bin/pg_config.libpq-dev by postgresql-common'

Unpacking postgresql-common (257build1) ...

Selecting previously unselected package libpopt0:arm64.

Preparing to unpack .../09-libpopt0_1.19+dfsg-1build1_arm64.deb ...

Unpacking libpopt0:arm64 (1.19+dfsg-1build1) ...

Selecting previously unselected package locales.

Preparing to unpack .../10-locales_2.39-0ubuntu8.1_all.deb ...

Unpacking locales (2.39-0ubuntu8.1) ...

Selecting previously unselected package logrotate.

Preparing to unpack .../11-logrotate_3.21.0-2build1_arm64.deb ...

Unpacking logrotate (3.21.0-2build1) ...

Selecting previously unselected package libsensors-config.

Preparing to unpack .../12-libsensors-config_1%3a3.6.0-9build1_all.deb ...

Unpacking libsensors-config (1:3.6.0-9build1) ...

Selecting previously unselected package libsensors5:arm64.

Preparing to unpack .../13-libsensors5_1%3a3.6.0-9build1_arm64.deb ...

Unpacking libsensors5:arm64 (1:3.6.0-9build1) ...

Selecting previously unselected package xz-utils.

Preparing to unpack .../14-xz-utils_5.6.1+really5.4.5-1_arm64.deb ...

Unpacking xz-utils (5.6.1+really5.4.5-1) ...

Selecting previously unselected package sysstat.

Preparing to unpack .../15-sysstat_12.6.1-2_arm64.deb ...

Unpacking sysstat (12.6.1-2) ...

Selecting previously unselected package libcommon-sense-perl:arm64.

Preparing to unpack .../16-libcommon-sense-perl_3.75-3build3_arm64.deb ...

Unpacking libcommon-sense-perl:arm64 (3.75-3build3) ...

Selecting previously unselected package libtypes-serialiser-perl.

Preparing to unpack .../17-libtypes-serialiser-perl_1.01-1_all.deb ...

Unpacking libtypes-serialiser-perl (1.01-1) ...

Selecting previously unselected package libjson-xs-perl.

Preparing to unpack .../18-libjson-xs-perl_4.030-2build3_arm64.deb ...

Unpacking libjson-xs-perl (4.030-2build3) ...

Selecting previously unselected package libldap-common.

Preparing to unpack .../19-libldap-common_2.6.7+dfsg-1~exp1ubuntu8_all.deb ...

Unpacking libldap-common (2.6.7+dfsg-1~exp1ubuntu8) ...

Selecting previously unselected package libsasl2-modules-db:arm64.

Preparing to unpack .../20-libsasl2-modules-db_2.1.28+dfsg1-5ubuntu3_arm64.deb ...

Unpacking libsasl2-modules-db:arm64 (2.1.28+dfsg1-5ubuntu3) ...

Selecting previously unselected package libsasl2-2:arm64.

Preparing to unpack .../21-libsasl2-2_2.1.28+dfsg1-5ubuntu3_arm64.deb ...

Unpacking libsasl2-2:arm64 (2.1.28+dfsg1-5ubuntu3) ...

Selecting previously unselected package libldap2:arm64.

Preparing to unpack .../22-libldap2_2.6.7+dfsg-1~exp1ubuntu8_arm64.deb ...

Unpacking libldap2:arm64 (2.6.7+dfsg-1~exp1ubuntu8) ...

Selecting previously unselected package libllvm17t64:arm64.

Preparing to unpack .../23-libllvm17t64_1%3a17.0.6-9ubuntu1_arm64.deb ...

Unpacking libllvm17t64:arm64 (1:17.0.6-9ubuntu1) ...

Selecting previously unselected package libpq5:arm64.

Preparing to unpack .../24-libpq5_16.2-1ubuntu4_arm64.deb ...

Unpacking libpq5:arm64 (16.2-1ubuntu4) ...

Selecting previously unselected package libsasl2-modules:arm64.

Preparing to unpack .../25-libsasl2-modules_2.1.28+dfsg1-5ubuntu3_arm64.deb ...

Unpacking libsasl2-modules:arm64 (2.1.28+dfsg1-5ubuntu3) ...

Selecting previously unselected package libxslt1.1:arm64.

Preparing to unpack .../26-libxslt1.1_1.1.39-0exp1build1_arm64.deb ...

Unpacking libxslt1.1:arm64 (1.1.39-0exp1build1) ...

Selecting previously unselected package postgresql-client-16.

Preparing to unpack .../27-postgresql-client-16_16.2-1ubuntu4_arm64.deb ...

Unpacking postgresql-client-16 (16.2-1ubuntu4) ...

Selecting previously unselected package postgresql-16.

Preparing to unpack .../28-postgresql-16_16.2-1ubuntu4_arm64.deb ...

Unpacking postgresql-16 (16.2-1ubuntu4) ...

Setting up libgdbm6t64:arm64 (1.23-5.1build1) ...

Setting up libgdbm-compat4t64:arm64 (1.23-5.1build1) ...

Setting up libsasl2-modules:arm64 (2.1.28+dfsg1-5ubuntu3) ...

Setting up libsensors-config (1:3.6.0-9build1) ...

Setting up locales (2.39-0ubuntu8.1) ...

debconf: unable to initialize frontend: Dialog

debconf: (Dialog frontend will not work on a dumb terminal, an emacs shell buffer, or without a controlling terminal.)

debconf: falling back to frontend: Readline

debconf: unable to initialize frontend: Readline

debconf: (This frontend requires a controlling tty.)

debconf: falling back to frontend: Teletype

Generating locales (this might take a while)...

Generation complete.

Setting up libldap-common (2.6.7+dfsg-1~exp1ubuntu8) ...

Setting up libsasl2-modules-db:arm64 (2.1.28+dfsg1-5ubuntu3) ...

Setting up libllvm17t64:arm64 (1:17.0.6-9ubuntu1) ...

Setting up ssl-cert (1.1.2ubuntu1) ...

debconf: unable to initialize frontend: Dialog

debconf: (Dialog frontend will not work on a dumb terminal, an emacs shell buffer, or without a controlling terminal.)

debconf: falling back to frontend: Readline

debconf: unable to initialize frontend: Readline

debconf: (This frontend requires a controlling tty.)

debconf: falling back to frontend: Teletype

Created symlink /etc/systemd/system/multi-user.target.wants/ssl-cert.service → /usr/lib/systemd/system/ssl-cert.service.

Setting up xz-utils (5.6.1+really5.4.5-1) ...

update-alternatives: using /usr/bin/xz to provide /usr/bin/lzma (lzma) in auto mode

update-alternatives: warning: skip creation of /usr/share/man/man1/lzma.1.gz because associated file /usr/share/man/man1/xz.1.gz (of link group lzma) doesn't exist

update-alternatives: warning: skip creation of /usr/share/man/man1/unlzma.1.gz because associated file /usr/share/man/man1/unxz.1.gz (of link group lzma) doesn't exist

update-alternatives: warning: skip creation of /usr/share/man/man1/lzcat.1.gz because associated file /usr/share/man/man1/xzcat.1.gz (of link group lzma) doesn't exist

update-alternatives: warning: skip creation of /usr/share/man/man1/lzmore.1.gz because associated file /usr/share/man/man1/xzmore.1.gz (of link group lzma) doesn't exist

update-alternatives: warning: skip creation of /usr/share/man/man1/lzless.1.gz because associated file /usr/share/man/man1/xzless.1.gz (of link group lzma) doesn't exist

update-alternatives: warning: skip creation of /usr/share/man/man1/lzdiff.1.gz because associated file /usr/share/man/man1/xzdiff.1.gz (of link group lzma) doesn't exist

update-alternatives: warning: skip creation of /usr/share/man/man1/lzcmp.1.gz because associated file /usr/share/man/man1/xzcmp.1.gz (of link group lzma) doesn't exist

update-alternatives: warning: skip creation of /usr/share/man/man1/lzgrep.1.gz because associated file /usr/share/man/man1/xzgrep.1.gz (of link group lzma) doesn't exist

update-alternatives: warning: skip creation of /usr/share/man/man1/lzegrep.1.gz because associated file /usr/share/man/man1/xzegrep.1.gz (of link group lzma) doesn't exist

update-alternatives: warning: skip creation of /usr/share/man/man1/lzfgrep.1.gz because associated file /usr/share/man/man1/xzfgrep.1.gz (of link group lzma) doesn't exist

Setting up perl-modules-5.38 (5.38.2-3.2build2) ...

Setting up libsensors5:arm64 (1:3.6.0-9build1) ...

Setting up libsasl2-2:arm64 (2.1.28+dfsg1-5ubuntu3) ...

Setting up libxslt1.1:arm64 (1.1.39-0exp1build1) ...

Setting up libperl5.38t64:arm64 (5.38.2-3.2build2) ...

Setting up sysstat (12.6.1-2) ...

debconf: unable to initialize frontend: Dialog

debconf: (Dialog frontend will not work on a dumb terminal, an emacs shell buffer, or without a controlling terminal.)

debconf: falling back to frontend: Readline

debconf: unable to initialize frontend: Readline

debconf: (This frontend requires a controlling tty.)

debconf: falling back to frontend: Teletype



Creating config file /etc/default/sysstat with new version

update-alternatives: using /usr/bin/sar.sysstat to provide /usr/bin/sar (sar) in auto mode

update-alternatives: warning: skip creation of /usr/share/man/man1/sar.1.gz because associated file /usr/share/man/man1/sar.sysstat.1.gz (of link group sar) doesn't exist

Created symlink /etc/systemd/system/sysstat.service.wants/sysstat-collect.timer → /usr/lib/systemd/system/sysstat-collect.timer.

Created symlink /etc/systemd/system/sysstat.service.wants/sysstat-summary.timer → /usr/lib/systemd/system/sysstat-summary.timer.

Created symlink /etc/systemd/system/multi-user.target.wants/sysstat.service → /usr/lib/systemd/system/sysstat.service.

Setting up libldap2:arm64 (2.6.7+dfsg-1~exp1ubuntu8) ...

Setting up libpopt0:arm64 (1.19+dfsg-1build1) ...

Setting up logrotate (3.21.0-2build1) ...

Created symlink /etc/systemd/system/timers.target.wants/logrotate.timer → /usr/lib/systemd/system/logrotate.timer.

Setting up libpq5:arm64 (16.2-1ubuntu4) ...

Setting up perl (5.38.2-3.2build2) ...

Setting up libjson-perl (4.10000-1) ...

Setting up postgresql-client-common (257build1) ...

Setting up postgresql-client-16 (16.2-1ubuntu4) ...

update-alternatives: using /usr/share/postgresql/16/man/man1/psql.1.gz to provide /usr/share/man/man1/psql.1.gz (psql.1.gz) in auto mode

Setting up libcommon-sense-perl:arm64 (3.75-3build3) ...

Setting up postgresql-common (257build1) ...

debconf: unable to initialize frontend: Dialog

debconf: (Dialog frontend will not work on a dumb terminal, an emacs shell buffer, or without a controlling terminal.)

debconf: falling back to frontend: Readline

debconf: unable to initialize frontend: Readline

debconf: (This frontend requires a controlling tty.)

debconf: falling back to frontend: Teletype



Creating config file /etc/postgresql-common/createcluster.conf with new version

Building PostgreSQL dictionaries from installed myspell/hunspell packages...

Removing obsolete dictionary files:

invoke-rc.d: could not determine current runlevel

invoke-rc.d: policy-rc.d denied execution of start.

Created symlink /etc/systemd/system/multi-user.target.wants/postgresql.service → /usr/lib/systemd/system/postgresql.service.

Setting up libtypes-serialiser-perl (1.01-1) ...

Setting up libjson-xs-perl (4.030-2build3) ...

Setting up postgresql-16 (16.2-1ubuntu4) ...

debconf: unable to initialize frontend: Dialog

debconf: (Dialog frontend will not work on a dumb terminal, an emacs shell buffer, or without a controlling terminal.)

debconf: falling back to frontend: Readline

debconf: unable to initialize frontend: Readline

debconf: (This frontend requires a controlling tty.)

debconf: falling back to frontend: Teletype

Creating new PostgreSQL cluster 16/main ...

/usr/lib/postgresql/16/bin/initdb -D /var/lib/postgresql/16/main --auth-local peer --auth-host scram-sha-256 --no-instructions

The files belonging to this database system will be owned by user "postgres".

This user must also own the server process.



The database cluster will be initialized with locale "C.UTF-8".

The default database encoding has accordingly been set to "UTF8".

The default text search configuration will be set to "english".



Data page checksums are disabled.



fixing permissions on existing directory /var/lib/postgresql/16/main ... ok

creating subdirectories ... ok

selecting dynamic shared memory implementation ... posix

selecting default max_connections ... 100

selecting default shared_buffers ... 128MB

selecting default time zone ... UTC

creating configuration files ... ok

running bootstrap script ... ok

performing post-bootstrap initialization ... ok

syncing data to disk ... ok

invoke-rc.d: could not determine current runlevel

invoke-rc.d: policy-rc.d denied execution of start.

Processing triggers for libc-bin (2.39-0ubuntu8.1) ...


PSQL insertion complete

2


echo -e "listen_addresses = '*'" >>  /etc/postgresql/16/main/postgresql.conf

sudo echo -e "host      all     all     0.0.0.0/0       password" >>  /etc/postgresql/16/main/pg_hba.conf

sudo service postgresql restart

sudo -u postgres psql -c "ALTER USER postgres WITH PASSWORD 'postgres'"

PSQL installing and configuring complete

1 - full_install_psql

2 - health_check
Enter your choice: 2

 ?column?

"------------"

        1

(1 row)


1 - full_install_psql

2 - health_check

Enter your choice: exit

Exiting program
---------