# RDA Development Environment for Apple Silicon

## Quick Start

```sh
docker compose up -d && docker compose exec solr wait-for-solr.sh && docker compose exec solr /bin/create-collections.sh && docker compose exec rda-registry /bin/fix-permissions.sh
```
The RDA Registry should now be accessible at http://localhost/

## Configuration

### Swap RDA Registry with another version

For M1 chipset `linux/arm64/v8`, make sure the `platform: linux/amd64` is set in the `docker-compose` service definition for `rda-registry` 

The `minhd/rda-registry` image comes with a standard version of RDA Registry, to swap to another version, simply mount them to the `rda-registry` container, for eg.

```yaml
# docker-compose.yml
  rda-registry:
    container_name: rda-registry
    image: minhd/rda-registry
    volumes:
      - /Users/minhd/dev/ardc/rda-registry:/opt/apps/registry/current
    ports:
      - "80:80"
```
Make sure the mounted `rda-registry/.env` file has the relevant connection information to the other services, an example of this can be found in the default configuration set at [rda-registry/conf/.env.rda-registry](rda-registry/conf/.env.rda-registry)
