BACKUP_DIR=/home/issjbrfs/swagbot2-run-dir/old-versions
INSTALL_DIRECTORY=/home/issjbrfs/swagbot2-run-dir
SRCS=bot.py
SRCS_TEST=bot_test.py
DATETIME := $(shell date +"%Y-%m-%d_%H-%M-%S")
BAK_TARGET := bot_$(DATETIME).py
all: release
clean:
	rm -f test/$(SRCS_TEST)
	rm -f test/$(SRCS_TEST).bak

tests:
	cp $(SRCS) test/$(SRCS_TEST)
	@TOKEN=$(shell cat tmptoken) && \
	sed -i.bak "s/YOUR TOKEN HERE/$${TOKEN}/g" test/$(SRCS_TEST)

install:
	mv $(INSTALL_DIRECTORY)/bot.py $(BACKUP_DIR)/$(BAK_TARGET)
	cp $(SRCS) $(INSTALL_DIRECTORY)/
	@TOKEN=$(shell cat tmptoken) && \
	sed -i.bak "s/YOUR TOKEN HERE/$${TOKEN}/g" $(INSTALL_DIRECTORY)/$(SRCS)

release:
	echo
