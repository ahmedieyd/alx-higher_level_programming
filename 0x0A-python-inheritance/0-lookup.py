def lookup(obj):
  """Returns a list of available attributes and methods of an object.

  Args:
    obj: Any object.

  Returns:
    A list of strings representing the available attributes and methods of the
    object.
  """

  attrs = []
  for name in dir(obj):
    if not name.startswith("__"):
      attrs.append(name)
  return attrs
