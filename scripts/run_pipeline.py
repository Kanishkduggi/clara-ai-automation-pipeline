import os
import subprocess


def run_script(script):

    print(f"\nRunning {script}...\n")

    result = subprocess.run(
        ["python", f"scripts/{script}"],
        capture_output=True,
        text=True
    )

    print(result.stdout)

    if result.stderr:
        print("Error:", result.stderr)


def run_pipeline():

    print("Starting Clara Automation Pipeline\n")

    # Step 1: Process demo transcripts
    run_script("extract_demo_data.py")

    # Step 2: Generate agent v1
    run_script("generate_agent_spec.py")

    # Step 3: Process onboarding updates
    run_script("update_from_onboarding.py")

    # Step 4: Generate agent v2
    run_script("generate_agent_spec.py")

    print("\nPipeline completed successfully.")


if __name__ == "__main__":
    run_pipeline()