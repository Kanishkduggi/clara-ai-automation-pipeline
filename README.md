```

# Clara AI Agent Automation Pipeline

This project automates the generation and versioning of AI voice agents using call transcripts.

## Architecture

The system processes transcripts in two stages:

1. Demo Calls → Generates initial agent configuration (v1)
2. Onboarding Calls → Updates agent configuration (v2)

Automation is orchestrated using Python scripts and an n8n workflow.

## Pipeline Steps

1. Extract structured data from demo transcripts
2. Generate agent specification (v1)
3. Process onboarding transcripts
4. Update agent specification (v2)
5. Generate changelog documenting updates

## Technologies Used

- Python
- JSON
- n8n Workflow Automation
- Docker

## Project Structure

dataset/ – demo and onboarding transcripts  
scripts/ – automation pipeline scripts  
outputs/ – generated agent configurations  
changelog/ – version history  
workflows/ – n8n automation workflow

## Running the Pipeline

Run the full automation pipeline:

python scripts/run_pipeline.py

## Workflow Automation

The project includes an n8n workflow that triggers the automation pipeline.

workflow file:

workflows/demo_pipeline.json

## Result

The pipeline generates:

- Agent version v1 from demo calls
- Updated agent version v2 from onboarding calls
- Changelog documenting modifications

## System Architecture

```
            +----------------------+
            |   n8n Workflow       |
            | (Automation Trigger) |
            +----------+-----------+
                       |
                       v
             +--------------------+
             |  Python Pipeline   |
             | run_pipeline.py    |
             +---------+----------+
                       |
     +-----------------+------------------+
     |                                    |
     v                                    v
+------------+                    +----------------+
| Demo Calls |                    | Onboarding Calls|
| dataset    |                    | dataset         |
+-----+------+                    +--------+--------+
      |                                    |
      v                                    v
extract_demo_data.py             update_from_onboarding.py
      |                                    |
      v                                    v
+--------------+                  +------------------+
| Agent Spec   |  ---> update --> | Agent Spec (v2)  |
| Version v1   |                  | Updated Config   |
+------+-------+                  +--------+---------+
       |                                   |
       v                                   v
           +------------------------------+
           |      Changelog Generator     |
           |   Documents agent updates    |
           +------------------------------+
```


## Key Features

* Automated extraction of business information from call transcripts
* Automatic AI agent configuration generation
* Versioned agent specifications (v1 → v2)
* Change tracking through generated changelogs
* Batch processing of multiple accounts
* Workflow automation using n8n


## Example Generated Agent Spec

```json
{
  "agent_name": "Service AI Agent",
  "voice_style": "professional",
  "version": "v2",
  "key_variables": {
    "business_hours": {
      "monday": "9am-5pm",
      "tuesday": "9am-5pm"
    },
    "services_supported": [
      "plumbing",
      "emergency repair"
    ]
  },
  "call_transfer_protocol": {
    "attempt_transfer": true,
    "timeout_seconds": 60
  }
}


## Limitations

* The extraction pipeline currently uses rule-based parsing instead of a local LLM.
* Demo transcripts must follow a relatively structured format for reliable extraction.
* The Retell agent configuration is generated as a JSON draft spec rather than automatically deployed through the Retell API.
* The n8n workflow currently acts as a trigger for the Python pipeline rather than executing each pipeline step individually.

## Future Improvements

If this system were deployed in production, the following improvements would be implemented:

* Replace rule-based extraction with a local LLM for more robust understanding of transcripts.
* Add a small dashboard to visualize accounts, versions, and configuration diffs.
* Store agent specifications in a database (Supabase or PostgreSQL) instead of local JSON files.
* Add automatic validation of extracted data to prevent malformed configurations.
* Implement a diff viewer to highlight changes between agent versions (v1 → v2).
* Add logging and monitoring for pipeline runs.

## Setup Instructions

1. Clone the repository.

2. Install Python dependencies (if required):

pip install -r requirements.txt

3. Ensure the dataset folder contains demo and onboarding transcripts.

4. Run the automation pipeline:

python scripts/run_pipeline.py

5. Generated outputs will appear in:

outputs/accounts/

Each account will contain:

* v1 agent specification generated from demo call
* v2 updated specification generated from onboarding call
* changelog describing modifications

```