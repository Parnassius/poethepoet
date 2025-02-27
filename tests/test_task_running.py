def test_ref_task(run_poe_subproc, projects, esc_prefix):
    # This should be exactly the same as calling the echo task directly
    result = run_poe_subproc("also_echo", "foo", "!")
    assert (
        result.capture
        == f"Poe => echo POE_ROOT:{projects['example']} Password1, task_args: foo !\n"
    )
    assert (
        result.stdout == f"POE_ROOT:{projects['example']} Password1, task_args: foo !\n"
    )
    assert result.stderr == ""
