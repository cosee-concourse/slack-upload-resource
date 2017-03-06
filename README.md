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

### `out`: Upload HTML files to Slack

* Uses a provided Bot token to upload html reports to slack. To generate unique 
  filenames the [semver](http://semver.org/) version is used.

#### Parameters
 
* `version`: *Required* Filepath to `semver` version file
* `directory`: *Required* Location of the html reports
* `channel`: *Required* The channel to upload the files to
* `SlACK_BOT_TOKEN`: *Required* Filepath to `semver` version file
* `command`: *Required* The type of message slack is supposed to send. Valid Arguments are `success`, `failure` and
  `report`.
* `pipeline_step`: *Required if `command` is `failure`* The current step of the pipeline so that the slack message can
   include at which stage of the pipeline the error occurred.


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
      command: report	
```
``` yaml
  - put: slack
    params: 
      version: version/number
      directory: junit
      SLACK_BOT_TOKEN: xoxb-1345678903412-xxxxxxxxxxxxxxxxxxxxxxxxx
      channel: bot-channel
      command: failure
      pipeline_step: build
```