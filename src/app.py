import redis
from datetime import timedelta
from flask import Flask, jsonify
from flask.blueprints import Blueprint
from flask_cors import CORS
from flask_jwt_extended import (
    JWTManager, create_access_token, create_refresh_token, get_jti,
    jwt_refresh_token_required, get_jwt_identity, jwt_required, get_raw_jwt
)

import config
import routes
import logging

server                                          = Flask(__name__)
server.config['JWT_SECRET_KEY']                 = config.JWT_SECRET_KEY
server.config['PROPAGATE_EXCEPTIONS']           = True
server.config['JWT_ACCESS_TOKEN_EXPIRES']       = timedelta(minutes=config.JWT_ACCESS_TOKEN_EXPIRY_IN_MINS)
server.config['JWT_REFRESH_TOKEN_EXPIRES']      = timedelta(days=config.JWT_REFRESH_TOKEN_EXPIRY_IN_DAYS)
server.config['JWT_BLACKLIST_ENABLED']          = True
server.config['JWT_BLACKLIST_TOKEN_CHECKS']     = ['access', 'refresh']

jwt                                             = JWTManager(server)

@jwt.user_claims_loader
def add_claims_to_access_token(identity):
    return {
        'username': identity['username'],
        'role': identity['role']
    }

@jwt.token_in_blacklist_loader
def check_if_token_is_valid(decrypted_token):
    jti                 = decrypted_token['jti']
    logging.debug('verifying token [%s] in redis-store' % (jti))

    try:
        revoked_store   = redis.StrictRedis(host=config.REDIS_HOSTNAME, port=config.REDIS_PORT, db=0, decode_responses=True)
        entry           = revoked_store.get(jti)
        logging.debug('token found %r' % (entry))

        if entry is None:
            return True
        if entry:
            return False
        return True

    except Exception as e:
        logging.error('connection redis failed with :%s' % (e))

if config.ENABLE_CORS:
    cors    = CORS(server, resources={r"/api/*": {"origins": "*"}})

for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        server.register_blueprint(blueprint, url_prefix=config.API_URL_PREFIX)

@server.route('/api/v1/info', methods=['GET'])
@jwt_required
def protected():
    return jsonify({
        'message': 'Welcome to FileServer API version 1.0',
    }), 200

if __name__ == "__main__":
    server.run(host=config.HOST, port=config.PORT)