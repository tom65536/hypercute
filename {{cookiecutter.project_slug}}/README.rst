{%- macro heading(text) -%}
{% for _ in text %}={% endfor %}
{{text}}
{% for _ in text %}={% endfor %}
{%- endmacro -%}
{{ heading(cookiecutter.project_slug) }}

