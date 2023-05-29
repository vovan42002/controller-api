ENV variables

| Name         | Type    | Description                  | Example                                               |
| -------------| --------| -----------------------------| ----------------------------------------------------- |
| DB_HOST      | String  | Postgresql host              | `localhost`, `192.168.0.1`                            |
| DB_USERNAME  | String  | Postgresql user              | `auth-user`                                           |
| DB_PASSWORD  | String  | Postgresql user password     | `Cahe8Quacjec3OmIgjomDagg`                            |
| DB_NAME      | String  | Postgresql db name           | `auth`                                                |
| DATABASE_URL | Url     | Postgresql connection string | `postgresql+asyncpg://user:password@host:5432/dbName` |

Build docker image

Example:

`docker build -t vovan4/controller-api:<tag> .`

Run docker container

Example:

`docker run --rm -p 8000:8000 --name controller-api --env DB_HOST="192.168.0.3" --env DB_USERNAME=postgres --env DB_PASSWORD=postgres --env DB_NAME=controller vovan4/controller-api:<tag>`

