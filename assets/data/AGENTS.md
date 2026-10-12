# Data Resource Rules

Read root RES_TYPE.md and the applicable definition under resource_templates/.
Use its selected format, identity, naming, properties, units and relationship rules.
Structured files must conform to their actual format; JSON does not permit comments.
Record numeric meaning in the schema, definition or companion documentation.

Preserve stable references and source/output provenance. Define absence/default
behavior where relevant; do not invent defaults for every optional field. Breaking
contract changes identify affected consumers and required migration. A resource
without a searchable reference may be dynamically loaded or intentionally retained;
do not delete it from that observation alone.

Root res_lib/ is the authoritative prepared library. Record any assets/data/ import
mapping in the type contract and live technical preferences. Engine copies and
source material remain identifiable. validate-assets.sh checks JSON syntax only;
use scoped audits for naming, schema, references and other actual requirements.
