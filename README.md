# Slack Upload Resource
 
[![Docker Repository on Quay](https://quay.io/repository/cosee-concourse/slack-upload-resource/status "Docker Repository on Quay")](https://quay.io/repository/cosee-concourse/slack-upload-resource)

Generates names for various services using a prefix and the current version.

## Source Configuration

* Not needed

## Behavior

### `check`: no-op

* Since this resource does not have a version itself `check` returns an empty JSON.

### `in`: no-op

* Simply returns the provided version

#### Parameters

* *None.*

### `out`: Upload artifacts as archive to the bucket.

* Uses a provided Bot token to upload html reports to slack. To generate unique 
  filenames the [semver](http://semver.org/) version is used.

#### Parameters
 
* `version`: *Required* Filepath to `semver` version file
* `directory`: *Required* Location of the html reports
* `channel`: *Required* The channel to upload the files to
* `SlACK_BOT_TOKEN`: *Required* Filepath to `semver` version file


## Example Configuration

### Resource Type
``` yaml
- name: slack-upload
  type: docker-image
  source:
    repository: quay.io/cosee-concourse/slack-upload-resource
```
### Resource

``` yaml
- name: slack
  type: slack-upload
```

### Plan

``` yaml
  - put: slack
    params: 
      version: version/number
      directory: junit
      SLACK_BOT_TOKEN: xoxb-1345678903412-xxxxxxxxxxxxxxxxxxxxxxxxx
	  channel: bot-channel	
```
