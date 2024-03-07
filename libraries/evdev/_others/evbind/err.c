#define _GNU_SOURCE
#include <stdarg.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "err.h"

struct evb_err {
	char *str;
	enum evb_err_num num;
};

struct evb_err *evb_err_new(void)
{
	struct evb_err *err;

	err = malloc(sizeof(struct evb_err));
	if (!err)
		return NULL;

	err->str = calloc(1, sizeof(char));
	if (!err->str) {
		free(err);
		return NULL;
	}

	evb_err_clr(err);

	return err;
}

void evb_err_free(struct evb_err *const err)
{
	free(err->str);
	free(err);
}

void evb_err_clr(struct evb_err *const err)
{
        /* Safe: str is always null terminated */
	memset(err->str, 0, strlen(err->str));
	err->num = EVB_ERR_NUM_NONE;
}

int evb_err_set(struct evb_err *const err, enum evb_err_num num,
		const char *const fmt, ...)
{
	char *str;
	va_list ap;

	va_start(ap, fmt);

	if (vasprintf(&str, fmt, ap) == -1) {
		va_end(ap);
		return -1;
	}

	va_end(ap);

	if (err->str)
		free(err->str);

	err->str = str;
	err->num = num;

	return 0;
}

enum evb_err_num evb_err_num(const struct evb_err *const err)
{
	return err->num;
}

const char *evb_err_str(const struct evb_err *const err)
{
	return err->str;
}
