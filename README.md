It occures this problem whene running:

docker-compose up --build

ERROR:

Traceback (most recent call last):
  File "/usr/bin/docker-compose", line 33, in <module>
    sys.exit(load_entry_point('docker-compose==1.29.2', 'console_scripts', 'docker-compose')())
  File "/usr/lib/python3/dist-packages/compose/cli/main.py", line 81, in main
    command_func()
  File "/usr/lib/python3/dist-packages/compose/cli/main.py", line 200, in perform_command
    project = project_from_options('.', options)
  File "/usr/lib/python3/dist-packages/compose/cli/command.py", line 40, in project_from_options
    environment = Environment.from_env_file(override_dir or project_dir, environment_file)
  File "/usr/lib/python3/dist-packages/compose/config/environment.py", line 67, in from_env_file
    instance = _initialize()
  File "/usr/lib/python3/dist-packages/compose/config/environment.py", line 62, in _initialize
    return cls(env_vars_from_file(env_file_path))
  File "/usr/lib/python3/dist-packages/compose/config/environment.py", line 38, in env_vars_from_file
    env = dotenv.dotenv_values(dotenv_path=filename, encoding='utf-8-sig', interpolate=interpolate)
  File "/usr/lib/python3/dist-packages/dotenv/main.py", line 364, in dotenv_values
    ).dict()
  File "/usr/lib/python3/dist-packages/dotenv/main.py", line 74, in dict
    self._dict = OrderedDict(resolve_variables(raw_values, override=self.override))
  File "/usr/lib/python3/dist-packages/dotenv/main.py", line 222, in resolve_variables
    for (name, value) in values:
  File "/usr/lib/python3/dist-packages/dotenv/main.py", line 82, in parse
    for mapping in with_warn_for_invalid_lines(parse_stream(stream)):
  File "/usr/lib/python3/dist-packages/dotenv/main.py", line 24, in with_warn_for_invalid_lines
    for mapping in mappings:
  File "/usr/lib/python3/dist-packages/dotenv/parser.py", line 180, in parse_stream
    reader = Reader(stream)
  File "/usr/lib/python3/dist-packages/dotenv/parser.py", line 71, in __init__
    self.string = stream.read()
  File "/usr/lib/python3.10/codecs.py", line 322, in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)
  File "/usr/lib/python3.10/encodings/utf_8_sig.py", line 69, in _buffer_decode
    return codecs.utf_8_decode(input, errors, final)
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa3 in position 15: invalid start byte
