
AF_QUERY_RETENTION_URL = 'https://hq1.appsflyer.com/connectivity/retention/data/'
AF_QUERY_INSTALL_URL = 'https://hq1.appsflyer.com/connectivity/vishnu/getAgg/'

AF_QUERY_PARAM_QUERY = 'query'
AF_QUERY_PARAM_START_TIME = 'start-time'
AF_QUERY_PARAM_END_TIME = 'end-time'
AF_QUERY_PARAM_GROUP = 'groupings'
AF_QUERY_PARAM_FILTER = 'filters'
AF_QUERY_PARAM_GRANULARITY = 'granularity'
AF_QUERY_PARAM_MIN_INSTALL = 'min-installs'
AF_QUERY_PARAM_TOPIC = 'topics'
AF_QUERY_PARAM_APP_ID = 'app_id'
AF_QUERY_PARAM_LIMIT = 'limit'
AF_QUERY_PARAM_START_DATE = 'start_date'
AF_QUERY_PARAM_END_DATE = 'end_date'

AF_GROUP_VALUE_MEDIA = 'media_source'
AF_GROUP_VALUE_COUNTRY = 'country'
AF_GROUP_VALUE_DATE = 'install_period'
AF_GROUP_VALUE_ADSET = 'adset'
AF_GROUP_VALUE_CAMPAIGN = 'campaign'

AF_FILTER_ATTRIBUTE_MEDIA = 'media_source'
AF_FILTER_ATTRIBUTE_COUNTRY = 'country'

AF_GRANULARITY_VALUE_DAILY = 'daily'

APP_ID_KWAI_ANDROID = 'com.smile.gifmaker'
APP_ID_KWAI_IOS = ''

COOKIE_KEY_HTTP_ONLY = 'httponly'
COOKIE_KEY_HTTP_EXPIRES = 'expires'
COOKIE_KEY_HTTP_EXPIRY = 'expiry'

RETENTION_KEY_ID = 'app_id'
RETENTION_KEY_NAME = 'app_name'
RETENTION_KEY_DATA = 'retention_data'

PARSE_KEY_DIMENSION = 'dimensions'
PARSE_KEY_MEDIA_SOURCE = 'media_source'
PARSE_KEY_COUNTRY = 'country'
PARSE_KEY_INSTALL_PERIOD = 'install_period'
PARSE_KEY_DATA = 'data'
PARSE_KEY_INSTALL = 'installs'
PARSE_KEY_CAMPAIGN = 'campaign'
PARSE_KEY_SESSION = 'sessions'
PARSE_KEY_LOYAL = 'loyals'


# example
#retention
# {"query":{"start-time":"2017-04-03","end-time":"2017-04-10","groupings":["media_source","country","install_period","adset"],"filters":{"media_source":["facebook"],"country":["AF","RU"]},"granularity":"daily","min-installs":1}}
#install
#{"query":{"app_id":"com.kwai.mercury","start_date":"2017-08-05","end_date":"2017-08-12","alt_timezone":false,"alt_currency":false,"tz_switch_date":"","filters":{"media_source":["googleadwords_int"]},"topics":["impressions","fb_impressions","clicks","fb_clicks","installs","sessions","loyals","install_cost","fb_spend","google_spend","inapps","uninstalls"],"post_processors":["revenue","conv_rate","loyal_rate","spend","roi","arpu","avg_ecpi","uninstall_rate"],"sort_by":[["installs","desc"]],"limit":50,"ms_timeout":54000,"remove_invalid_topics":true,"groupings":["campaign","event_name"]}}

#error
#{"error":"'Query Problems: {:topics [(not (#{\"ctit_minutes\" \"installs\" \"impressions\" \"ltv\" \"sessions\" \"inapps\" \"fb_impressions\" \"partners\" \"clicks\" \"uninstalls\" \"dummy_topic\" \"ctit_seconds\" \"install_cost\" \"loyals\" \"fb_spend\" \"fb_clicks\" \"assists\" \"master\" \"ctit_hours\" \"failing_topic\" \"ctit_days\" \"google_spend\"} \"install\")) (not (#{\"ctit_minutes\" \"installs\" \"impressions\" \"ltv\" \"sessions\" \"inapps\" \"fb_impressions\" \"partners\" \"clicks\" \"uninstalls\" \"dummy_topic\" \"ctit_seconds\" \"install_cost\" \"loyals\" \"fb_spend\" \"fb_clicks\" \"assists\" \"master\" \"ctit_hours\" \"failing_topic\" \"ctit_days\" \"google_spend\"} \"session\")) nil], :end_date missing-required-key, :start_date missing-required-key, :end-time disallowed-key, :start-time disallowed-key}\nQuery Params{:end-time \"2017-08-12\", :start-time \"2017-08-12\", :topics [\"install\" \"session\" \"loyals\"], :limit 2000, :filters {:media_source [\"googleadwords_int\"]}, :groupings [\"campaign\"], :viewing_partner \"EliAds\", :transparent_agencies {\"id1152332968\" [\"cyberagent-rin\" \"Adways\"], \"com.uc.iflow\" [\"AmbientIndonesia\"], \"com.ss.android.article.topbuzzvideo\" [\"Adways\" \"cyberagent-rin\"]}, :app_id \"com.kwai.mercury\"}'"}