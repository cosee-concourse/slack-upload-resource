# Slack Upload Resource
 
[![Docker Repository on Quay](https://quay.io/repository/cosee-concourse/slack-upload-resource/status "Docker Repository on Quay")](https://quay.io/repository/cosee-concourse/slack-upload-resource)

Generates names for various services using a prefix and the current version.

## Source Configuration

* `SlACK_BOT_TOKEN`: *Required* Token for Slack Bot that should be used to post messages

## Behavior

### `out`: Post messages to Slack

* Posts a message to slack based on the command provided. To give better information on the state of the pipeline 
  the [semver](http://semver.org/) version is used.
  
### `check`: no-op

* Since this resource does not have a version itself `check` returns an empty JSON.

### `in`: no-op

* Simply returns the provided version


#### Parameters
 
* `version`: *Required* Filepath to `semver` version file
* `command`: *Required* The type of message slack is supposed to send. Valid Arguments are `success`, `failure` and
  `report`.
* `directory`: *Required if command is `report`* Location of the html reports
* `channel`: *Required* The channel for the message to appear in
* `pipeline_step`: *Required* The current step of the pipeline so that the slack message can
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
  source: 
    SLACK_BOT_TOKEN: xoxb-1345678903412-xxxxxxxxxxxxxxxxxxxxxxxxx
```

### Plan

``` yaml
  - put: slack
    params: 
      version: version/number
      command: report
      directory: junit
      channel: bot-channel
```
``` yaml
  - put: slack
    params: 
      version: version/number
      command: failure
      channel: bot-channel
      pipeline_step: build
```