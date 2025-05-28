BACKUP_DIR=/home/oskar/swagbot2-run-dir/old-versions
INSTALL_DIRECTORY=/home/oskar/swagbot2-run-dir
SYSTEM_LOGS_DIR="/home/oskar/swagbot2-run-dir/pitroles"
SYSTEM_BAD_WORDS_DIR="/home/oskar/swagbot2-run-dir/bannedwords"
MISC_DIR=misc
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
	sed -i "s#YOUR LOG PATH#$(SYSTEM_LOGS_DIR)#g" test/$(SRCS_TEST)
	sed -i "s#YOUR BAD WORDS PATH#$(SYSTEM_BAD_WORDS_DIR)#g" test/$(SRCS_TEST)

install:
	mv $(INSTALL_DIRECTORY)/bot.py $(BACKUP_DIR)/$(BAK_TARGET)
	cp $(SRCS) $(INSTALL_DIRECTORY)/
	cp -r $(MISC_DIR) $(INSTALL_DIRECTORY)/
	@TOKEN=$(shell cat tmptoken) && \
	sed -i.bak "s/YOUR TOKEN HERE/$${TOKEN}/g" $(INSTALL_DIRECTORY)/$(SRCS)
	@COMMIT_HASH=$(shell git rev-parse HEAD) && \
	sed -i.bak "s/TESTING_VERSION/$${COMMIT_HASH}/g" $(INSTALL_DIRECTORY)/$(SRCS)
	sed -i "s#YOUR LOG PATH#$(SYSTEM_LOGS_DIR)#g" $(INSTALL_DIRECTORY)/$(SRCS)
	sed -i "s#YOUR BAD WORDS PATH#$(SYSTEM_BAD_WORDS_DIR)#g" $(INSTALL_DIRECTORY)/$(SRCS)

release:
	echo
