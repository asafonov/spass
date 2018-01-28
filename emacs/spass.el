(defun spass-get(account)
  (interactive "sPlease specify the account: ")
  (setq password (shell-command-to-string (concat "spass --print --get " account)))
  (kill-new password)
  (message "Done")
)
(defun spass-update(account)
  (interactive "sPlease specify the account: ")
  (setq password (shell-command-to-string (concat "spass --update " account)))
  (kill-new password)
  (message "Done")
)
(defun spass-update-simple(account)
  (interactive "sPlease specify the account: ")
  (setq password (shell-command-to-string (concat "spass --simple --update " account)))
  (kill-new password)
  (message "Done")
)
(defun spass-delete(account)
  (interactive "sPlease specify the account: ")
  (shell-command (concat "spass --delete " account))
  (message "Done")
)
(defun spass-set(account password)
  (interactive "sPlease specify the account: \nsEnter password: ")
  (shell-command (concat "spass --set " account " --password " password))
  (message "Done")
)
(defun spass-export(filename)
  (interactive "fPlease specify filename for export: ")
  (shell-command (concat "spass --export --file " filename))
  (message "Done")
)
(defun spass-import(filename)
  (interactive "fPlease specify filename for import: ")
  (shell-command (concat "spass --import --file " filename))
  (message "Done")
)
(defun spass-export-key(filename key)
  (interactive "fPlease specify filename for export: \nsEnter encryption key: ")
  (shell-command (concat "spass --export --key " key " --file " filename))
  (message "Done")
)
(defun spass-import-key(filename key)
  (interactive "fPlease specify filename for import: \nsEnter decription key: ")
  (shell-command (concat "spass --import --key " key " --file " filename))
  (message "Done")
)
(defun spass-set-password(password)
  (interactive "sEnter password: ")
  (shell-command (concat "spass --set-password " filename))
  (message "Done")
)

(provide 'spass)
