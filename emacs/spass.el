(defun spass-get(account)
  (interactive "sPlease specify the account: ")
  (setq password (shell-command-to-string (concat "spass --get --account " account)))
  (kill-new password)
  (message "Done")
)
(defun spass-update(account)
  (interactive "sPlease specify the account: ")
  (setq password (shell-command-to-string (concat "spass --update --account " account)))
  (kill-new password)
  (message "Done")
)
(defun spass-set(account  password)
  (interactive "sPlease specify the account: \nsEnter password: ")
  (setq password (shell-command-to-string (concat "spass --set --account " account " --password " password)))
  (kill-new password)
  (message "Done")
)

(provide 'spass)
