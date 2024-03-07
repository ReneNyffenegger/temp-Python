enum evb_err_num {
	EVB_ERR_NUM_NONE,
	EVB_ERR_NUM_SYS,
	EVB_ERR_NUM_UNKNOWN,
	EVB_ERR_NUM_UDEV
};

struct evb_err;

struct evb_err *evb_err_new(void);
void evb_err_free(struct evb_err *err);

void evb_err_clr(struct evb_err *err);
int evb_err_set(struct evb_err *err, enum evb_err_num num,
		const char *fmt, ...);
enum evb_err_num evb_err_num(const struct evb_err *err);
const char *evb_err_str(const struct evb_err *err);
