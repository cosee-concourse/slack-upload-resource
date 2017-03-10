source_schema = {
    "type": "object",
    "properties": {
        "SLACK_BOT_TOKEN": {
            "type": "string"
        }
    },
    "required": [
        "SLACK_BOT_TOKEN"
    ]
}

version_schema = {
    "oneOf": [{
        "type": "object",
        "properties": {
            "schema": {
                "type": "string"
            }
        }
    }, {
        "type": "null"
    }]
}

check_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "source": source_schema,
        "version": version_schema
    },
    "required": [
        "source"
    ]
}

out_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "source": source_schema,
        "params": {
            "type": "object",
            "oneOf": [
                {"properties": {
                    "version": {
                        "type": "string"
                    },
                    "command": {
                        "type": "string",
                        "enum": ["success", "failure"]
                    },
                    "channel": {
                        "type": "string"
                    },
                    "pipeline_step": {
                        "type": "string"
                    },
                },
                "required": [
                  "version",
                  "command",
                  "channel",
                  "pipeline_step"
                ]},
                {"properties": {
                    "version": {
                        "type": "string"
                    },
                    "command": {
                        "type": "string",
                        "enum": ["report"]
                    },
                    "directory": {
                        "type": "string"
                    },
                    "channel": {
                        "type": "string"
                    },
                    "pipeline_step": {
                        "type": "string"
                    },
                },
                "required": [
                  "version",
                  "command",
                  "channel",
                  "directory",
                  "pipeline_step"
                ]}],
                "additionalProperties": "false"
        }
    },
    "required": [
        "source",
        "params"
    ]
}

in_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "source": source_schema,
        "version": version_schema
    },
    "required": [
        "source",
        "version"
    ]
}