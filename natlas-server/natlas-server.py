from app import create_app, db
from app.models import User, ScopeItem, ConfigItem, NatlasServices, AgentConfig, RescanTask, \
	Tag, Agent, AgentScript, EmailToken


app = create_app(load_config=True)


@app.shell_context_processor
def make_shell_context():
	return {
		'db': db,
		'User': User,
		'ScopeItem': ScopeItem,
		'ConfigItem': ConfigItem,
		'NatlasServices': NatlasServices,
		'AgentConfig': AgentConfig,
		'RescanTask': RescanTask,
		'Tag': Tag,
		'Agent': Agent,
		'AgentScript': AgentScript,
		'EmailToken': EmailToken
	}
