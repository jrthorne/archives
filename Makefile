ROUSER := jason
ROHOST := 119.9.40.12
RODIR := /www

RSYNC_OPTIONS := --verbose \
	--checksum \
	--recursive \
	--links \
	--times \
	--perms \
	--cvs-exclude \
	--compress \
	--exclude-from=NOROLLOUT

.PHONY: all rollout committed update

all:

committed:
	@if [ `svn st | wc -l` -gt 0]; then\
		echo -en "\\033[1;31m"; \
		echo "  **********************************************";\
		echo "  you still have modified files not checked in";\
		echo "  **********************************************";\
		echo -en "\\033[0;39m";

	fi

update:
	svn up
	@if svn st | grep -q ^C ; then \
		echo -en "\\033[1;31m"; \
		echo "  *********************************"; \
		echo "  conflicts exist!"; \
		echo "  *********************************"; \
		echo -en "\\033[1;39m"; \
		false;\
	fi


rollout:
	rsync $(RSYNC_OPTIONS) ../archeologist $(ROUSER)@$(ROHOST):$(RODIR)/
	@echo "\\033[1;32m"
	@echo "  =================================================="
	@echo -n "   Rollout time is "
	@date
	@echo "  =================================================="
	@echo "\\033[0;39m";

clean:	
	rsync $(RSYNC_OPTIONS) --delete ../archeologist $(ROUSER)@$(ROHOST):$(RODIR)/
	@echo "\\033[1;32m"
	@echo "  =================================================="
	@echo -n "   Rollout with delete time is "
	@date
	@echo "  =================================================="
	@echo "\\033[0;39m";

