# Task 4: Set Access Rights and Access Rules

## Description
Define role-based access rights in the `security/` directory for the `dudoxx_automation` module.

## Steps Taken
1. Created `ir.model.access.csv` with access rights for the `dudoxx.task` model:
   ```csv
   id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
   access_dudoxx_task_user,access_dudoxx_task_user,model_dudoxx_task,,1,1,1,1
   ```

2. Defined access rules in `security/access_rules.xml` for different roles:
   ```xml
   <record id="rule_dudoxx_task_user" model="ir.rule">
       <field name="name">Dudoxx Task User</field>
       <field name="model_id" ref="model_dudoxx_task"/>
       <field name="groups" eval="[(4, ref('base.group_user'))]"/>
       <field name="domain_force">[('status', '=', 'in_progress')]</field>
   </record>
   ```

## Outcome
Access rights and rules are established, allowing users to interact with the `dudoxx.task` model based on their roles.
