# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['test_create_execution_plan_with_dep 1'] = '''{
  "__class__": "ExecutionPlanSnapshot",
  "artifacts_persisted": true,
  "executor_name": "in_process",
  "initial_known_state": null,
  "pipeline_snapshot_id": "dafacc9dca12bc6d87e5602b885aaaf49dd4ad80",
  "snapshot_version": 1,
  "step_keys_to_execute": [
    "solid_one",
    "solid_two"
  ],
  "steps": [
    {
      "__class__": "ExecutionStepSnap",
      "inputs": [],
      "key": "solid_one",
      "kind": {
        "__enum__": "StepKind.COMPUTE"
      },
      "metadata_items": [],
      "outputs": [
        {
          "__class__": "ExecutionStepOutputSnap",
          "dagster_type_key": "Any",
          "name": "result",
          "properties": {
            "__class__": "StepOutputProperties",
            "is_asset": false,
            "is_dynamic": false,
            "is_required": true,
            "should_materialize": false
          },
          "solid_handle": {
            "__class__": "SolidHandle",
            "name": "solid_one",
            "parent": null
          }
        }
      ],
      "solid_handle_id": "solid_one",
      "step_handle": {
        "__class__": "StepHandle",
        "key": "solid_one",
        "solid_handle": {
          "__class__": "SolidHandle",
          "name": "solid_one",
          "parent": null
        }
      },
      "tags": {}
    },
    {
      "__class__": "ExecutionStepSnap",
      "inputs": [
        {
          "__class__": "ExecutionStepInputSnap",
          "dagster_type_key": "Any",
          "name": "num",
          "source": {
            "__class__": "FromStepOutput",
            "fan_in": false,
            "input_name": "num",
            "solid_handle": {
              "__class__": "SolidHandle",
              "name": "solid_two",
              "parent": null
            },
            "step_output_handle": {
              "__class__": "StepOutputHandle",
              "mapping_key": null,
              "output_name": "result",
              "step_key": "solid_one"
            }
          },
          "upstream_output_handles": [
            {
              "__class__": "StepOutputHandle",
              "mapping_key": null,
              "output_name": "result",
              "step_key": "solid_one"
            }
          ]
        }
      ],
      "key": "solid_two",
      "kind": {
        "__enum__": "StepKind.COMPUTE"
      },
      "metadata_items": [],
      "outputs": [
        {
          "__class__": "ExecutionStepOutputSnap",
          "dagster_type_key": "Any",
          "name": "result",
          "properties": {
            "__class__": "StepOutputProperties",
            "is_asset": false,
            "is_dynamic": false,
            "is_required": true,
            "should_materialize": false
          },
          "solid_handle": {
            "__class__": "SolidHandle",
            "name": "solid_two",
            "parent": null
          }
        }
      ],
      "solid_handle_id": "solid_two",
      "step_handle": {
        "__class__": "StepHandle",
        "key": "solid_two",
        "solid_handle": {
          "__class__": "SolidHandle",
          "name": "solid_two",
          "parent": null
        }
      },
      "tags": {}
    }
  ]
}'''

snapshots['test_create_noop_execution_plan 1'] = '''{
  "__class__": "ExecutionPlanSnapshot",
  "artifacts_persisted": true,
  "executor_name": "in_process",
  "initial_known_state": null,
  "pipeline_snapshot_id": "65cbb3805d12531e03977a0760c103ee6d519111",
  "snapshot_version": 1,
  "step_keys_to_execute": [
    "noop_solid"
  ],
  "steps": [
    {
      "__class__": "ExecutionStepSnap",
      "inputs": [],
      "key": "noop_solid",
      "kind": {
        "__enum__": "StepKind.COMPUTE"
      },
      "metadata_items": [],
      "outputs": [
        {
          "__class__": "ExecutionStepOutputSnap",
          "dagster_type_key": "Any",
          "name": "result",
          "properties": {
            "__class__": "StepOutputProperties",
            "is_asset": false,
            "is_dynamic": false,
            "is_required": true,
            "should_materialize": false
          },
          "solid_handle": {
            "__class__": "SolidHandle",
            "name": "noop_solid",
            "parent": null
          }
        }
      ],
      "solid_handle_id": "noop_solid",
      "step_handle": {
        "__class__": "StepHandle",
        "key": "noop_solid",
        "solid_handle": {
          "__class__": "SolidHandle",
          "name": "noop_solid",
          "parent": null
        }
      },
      "tags": {}
    }
  ]
}'''

snapshots['test_create_noop_execution_plan_with_tags 1'] = '''{
  "__class__": "ExecutionPlanSnapshot",
  "artifacts_persisted": true,
  "executor_name": "in_process",
  "initial_known_state": null,
  "pipeline_snapshot_id": "ef7c1096d29a9608e7ac0a06ce44519b101742ee",
  "snapshot_version": 1,
  "step_keys_to_execute": [
    "noop_solid"
  ],
  "steps": [
    {
      "__class__": "ExecutionStepSnap",
      "inputs": [],
      "key": "noop_solid",
      "kind": {
        "__enum__": "StepKind.COMPUTE"
      },
      "metadata_items": [
        {
          "__class__": "ExecutionPlanMetadataItemSnap",
          "key": "bar",
          "value": "baaz"
        },
        {
          "__class__": "ExecutionPlanMetadataItemSnap",
          "key": "foo",
          "value": "bar"
        }
      ],
      "outputs": [
        {
          "__class__": "ExecutionStepOutputSnap",
          "dagster_type_key": "Any",
          "name": "result",
          "properties": {
            "__class__": "StepOutputProperties",
            "is_asset": false,
            "is_dynamic": false,
            "is_required": true,
            "should_materialize": false
          },
          "solid_handle": {
            "__class__": "SolidHandle",
            "name": "noop_solid",
            "parent": null
          }
        }
      ],
      "solid_handle_id": "noop_solid",
      "step_handle": {
        "__class__": "StepHandle",
        "key": "noop_solid",
        "solid_handle": {
          "__class__": "SolidHandle",
          "name": "noop_solid",
          "parent": null
        }
      },
      "tags": {
        "bar": "baaz",
        "foo": "bar"
      }
    }
  ]
}'''

snapshots['test_create_with_composite 1'] = '''{
  "__class__": "ExecutionPlanSnapshot",
  "artifacts_persisted": true,
  "executor_name": "in_process",
  "initial_known_state": null,
  "pipeline_snapshot_id": "23a511c9b11c6c4cec82b58cb7f63818ada3b373",
  "snapshot_version": 1,
  "step_keys_to_execute": [
    "comp_1.return_one",
    "comp_1.add_one",
    "comp_2.return_one",
    "comp_2.add_one",
    "add"
  ],
  "steps": [
    {
      "__class__": "ExecutionStepSnap",
      "inputs": [
        {
          "__class__": "ExecutionStepInputSnap",
          "dagster_type_key": "Any",
          "name": "num_one",
          "source": {
            "__class__": "FromStepOutput",
            "fan_in": false,
            "input_name": "num_one",
            "solid_handle": {
              "__class__": "SolidHandle",
              "name": "add",
              "parent": null
            },
            "step_output_handle": {
              "__class__": "StepOutputHandle",
              "mapping_key": null,
              "output_name": "result",
              "step_key": "comp_1.add_one"
            }
          },
          "upstream_output_handles": [
            {
              "__class__": "StepOutputHandle",
              "mapping_key": null,
              "output_name": "result",
              "step_key": "comp_1.add_one"
            }
          ]
        },
        {
          "__class__": "ExecutionStepInputSnap",
          "dagster_type_key": "Any",
          "name": "num_two",
          "source": {
            "__class__": "FromStepOutput",
            "fan_in": false,
            "input_name": "num_two",
            "solid_handle": {
              "__class__": "SolidHandle",
              "name": "add",
              "parent": null
            },
            "step_output_handle": {
              "__class__": "StepOutputHandle",
              "mapping_key": null,
              "output_name": "result",
              "step_key": "comp_2.add_one"
            }
          },
          "upstream_output_handles": [
            {
              "__class__": "StepOutputHandle",
              "mapping_key": null,
              "output_name": "result",
              "step_key": "comp_2.add_one"
            }
          ]
        }
      ],
      "key": "add",
      "kind": {
        "__enum__": "StepKind.COMPUTE"
      },
      "metadata_items": [],
      "outputs": [
        {
          "__class__": "ExecutionStepOutputSnap",
          "dagster_type_key": "Any",
          "name": "result",
          "properties": {
            "__class__": "StepOutputProperties",
            "is_asset": false,
            "is_dynamic": false,
            "is_required": true,
            "should_materialize": false
          },
          "solid_handle": {
            "__class__": "SolidHandle",
            "name": "add",
            "parent": null
          }
        }
      ],
      "solid_handle_id": "add",
      "step_handle": {
        "__class__": "StepHandle",
        "key": "add",
        "solid_handle": {
          "__class__": "SolidHandle",
          "name": "add",
          "parent": null
        }
      },
      "tags": {}
    },
    {
      "__class__": "ExecutionStepSnap",
      "inputs": [
        {
          "__class__": "ExecutionStepInputSnap",
          "dagster_type_key": "Int",
          "name": "num",
          "source": {
            "__class__": "FromStepOutput",
            "fan_in": false,
            "input_name": "num",
            "solid_handle": {
              "__class__": "SolidHandle",
              "name": "add_one",
              "parent": {
                "__class__": "SolidHandle",
                "name": "comp_1",
                "parent": null
              }
            },
            "step_output_handle": {
              "__class__": "StepOutputHandle",
              "mapping_key": null,
              "output_name": "out_num",
              "step_key": "comp_1.return_one"
            }
          },
          "upstream_output_handles": [
            {
              "__class__": "StepOutputHandle",
              "mapping_key": null,
              "output_name": "out_num",
              "step_key": "comp_1.return_one"
            }
          ]
        }
      ],
      "key": "comp_1.add_one",
      "kind": {
        "__enum__": "StepKind.COMPUTE"
      },
      "metadata_items": [],
      "outputs": [
        {
          "__class__": "ExecutionStepOutputSnap",
          "dagster_type_key": "Int",
          "name": "result",
          "properties": {
            "__class__": "StepOutputProperties",
            "is_asset": false,
            "is_dynamic": false,
            "is_required": true,
            "should_materialize": false
          },
          "solid_handle": {
            "__class__": "SolidHandle",
            "name": "add_one",
            "parent": {
              "__class__": "SolidHandle",
              "name": "comp_1",
              "parent": null
            }
          }
        }
      ],
      "solid_handle_id": "comp_1.add_one",
      "step_handle": {
        "__class__": "StepHandle",
        "key": "comp_1.add_one",
        "solid_handle": {
          "__class__": "SolidHandle",
          "name": "add_one",
          "parent": {
            "__class__": "SolidHandle",
            "name": "comp_1",
            "parent": null
          }
        }
      },
      "tags": {}
    },
    {
      "__class__": "ExecutionStepSnap",
      "inputs": [],
      "key": "comp_1.return_one",
      "kind": {
        "__enum__": "StepKind.COMPUTE"
      },
      "metadata_items": [],
      "outputs": [
        {
          "__class__": "ExecutionStepOutputSnap",
          "dagster_type_key": "Int",
          "name": "out_num",
          "properties": {
            "__class__": "StepOutputProperties",
            "is_asset": false,
            "is_dynamic": false,
            "is_required": true,
            "should_materialize": false
          },
          "solid_handle": {
            "__class__": "SolidHandle",
            "name": "return_one",
            "parent": {
              "__class__": "SolidHandle",
              "name": "comp_1",
              "parent": null
            }
          }
        }
      ],
      "solid_handle_id": "comp_1.return_one",
      "step_handle": {
        "__class__": "StepHandle",
        "key": "comp_1.return_one",
        "solid_handle": {
          "__class__": "SolidHandle",
          "name": "return_one",
          "parent": {
            "__class__": "SolidHandle",
            "name": "comp_1",
            "parent": null
          }
        }
      },
      "tags": {}
    },
    {
      "__class__": "ExecutionStepSnap",
      "inputs": [
        {
          "__class__": "ExecutionStepInputSnap",
          "dagster_type_key": "Int",
          "name": "num",
          "source": {
            "__class__": "FromStepOutput",
            "fan_in": false,
            "input_name": "num",
            "solid_handle": {
              "__class__": "SolidHandle",
              "name": "add_one",
              "parent": {
                "__class__": "SolidHandle",
                "name": "comp_2",
                "parent": null
              }
            },
            "step_output_handle": {
              "__class__": "StepOutputHandle",
              "mapping_key": null,
              "output_name": "out_num",
              "step_key": "comp_2.return_one"
            }
          },
          "upstream_output_handles": [
            {
              "__class__": "StepOutputHandle",
              "mapping_key": null,
              "output_name": "out_num",
              "step_key": "comp_2.return_one"
            }
          ]
        }
      ],
      "key": "comp_2.add_one",
      "kind": {
        "__enum__": "StepKind.COMPUTE"
      },
      "metadata_items": [],
      "outputs": [
        {
          "__class__": "ExecutionStepOutputSnap",
          "dagster_type_key": "Int",
          "name": "result",
          "properties": {
            "__class__": "StepOutputProperties",
            "is_asset": false,
            "is_dynamic": false,
            "is_required": true,
            "should_materialize": false
          },
          "solid_handle": {
            "__class__": "SolidHandle",
            "name": "add_one",
            "parent": {
              "__class__": "SolidHandle",
              "name": "comp_2",
              "parent": null
            }
          }
        }
      ],
      "solid_handle_id": "comp_2.add_one",
      "step_handle": {
        "__class__": "StepHandle",
        "key": "comp_2.add_one",
        "solid_handle": {
          "__class__": "SolidHandle",
          "name": "add_one",
          "parent": {
            "__class__": "SolidHandle",
            "name": "comp_2",
            "parent": null
          }
        }
      },
      "tags": {}
    },
    {
      "__class__": "ExecutionStepSnap",
      "inputs": [],
      "key": "comp_2.return_one",
      "kind": {
        "__enum__": "StepKind.COMPUTE"
      },
      "metadata_items": [],
      "outputs": [
        {
          "__class__": "ExecutionStepOutputSnap",
          "dagster_type_key": "Int",
          "name": "out_num",
          "properties": {
            "__class__": "StepOutputProperties",
            "is_asset": false,
            "is_dynamic": false,
            "is_required": true,
            "should_materialize": false
          },
          "solid_handle": {
            "__class__": "SolidHandle",
            "name": "return_one",
            "parent": {
              "__class__": "SolidHandle",
              "name": "comp_2",
              "parent": null
            }
          }
        }
      ],
      "solid_handle_id": "comp_2.return_one",
      "step_handle": {
        "__class__": "StepHandle",
        "key": "comp_2.return_one",
        "solid_handle": {
          "__class__": "SolidHandle",
          "name": "return_one",
          "parent": {
            "__class__": "SolidHandle",
            "name": "comp_2",
            "parent": null
          }
        }
      },
      "tags": {}
    }
  ]
}'''
