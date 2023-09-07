# python_sources()

python_requirements(
    name="reqs",
)

# python_sources(
#     name="lib",
#     dependencies=[
#         "edmmp/service_a",
#     ],
#     overrides={
#         "manage.py": {
#             "dependencies": ["edmmp/service_a/service_a/settings.py:lib"],
#             "restartable": True,
#         },
#     },
# )

pex_binary(
    name="app",
    entry_point="manage.py",
    # dependencies=[
    #     ":lib",
    # ],
)