from ...core.validators import validate_one_of_args_is_in_query
from . import from_global_id_or_error


def resolve_by_global_id_or_ext_ref(model, id, ext_ref):
    validate_one_of_args_is_in_query("id", id, "external_reference", ext_ref)
    if id:
        _, id = from_global_id_or_error(id, model.__name__)
        return model.objects.filter(id=id).first()
    else:
        return model.objects.filter(external_reference=ext_ref).first()


def resolve_by_global_id_slug_or_ext_ref(model, id, slug, ext_ref):
    validate_one_of_args_is_in_query(
        "id", id, "slug", slug, "external_reference", ext_ref
    )
    if id:
        _, id = from_global_id_or_error(id, model.__name__)
        return model.objects.filter(id=id).first()
    elif slug:
        return model.objects.filter(slug=slug).first()
    else:
        return model.objects.filter(external_reference=ext_ref).first()
