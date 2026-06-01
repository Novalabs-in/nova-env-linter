import os

class EnvConfigLinter:
    """
    Environment Template Configuration Linter
    Validates that all environment variable declarations are present.
    """
    def lint_env(self, active_vars, expected_vars):
        missing = [v for v in expected_vars if v not in active_vars]
        return missing

if __name__ == "__main__":
    linter = EnvConfigLinter()
    missing = linter.lint_env({"PORT": "3000"}, ["PORT", "DATABASE_URL"])
    print("Security environment lints complete. Missing variables:", missing)
